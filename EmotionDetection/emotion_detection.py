import requests
import json

def emotion_detector(text_to_analyze):
    """
    function to run emotion detection
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 500:
        output = {
            'anger': none,
            'disgust': none,
            'fear': none,
            'joy': none,
            'sadness': none,
            'dominant_emotion': none
        }
    
    return output
