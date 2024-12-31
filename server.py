"""
application port : 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detector():
    """
    This code receives the text from the HTML interface and 
    runs detect emotion over it using emotion_detector()
    function.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is \'anger\': {anger}, \
    \'disgust\': {disgust}, \'fear\': {fear}, \'joy\': {joy}, and \'sadness\': {sadness}. \
    The dominant emotion is <strong>{dominant_emotion}</strong>."

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
