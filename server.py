"""
This module is used to detect user emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    A Flask route to detect emotions from input text.
    This function serves as the endpoint for the emotion detection service.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Try again."
    return (f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>.")

@app.route("/")
def render_index_page():
    """
    This function serves as the endpoint for index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
