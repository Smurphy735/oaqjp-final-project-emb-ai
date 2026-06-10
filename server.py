"""
server.py

Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app by the name Emotion Detector
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Handle emotion detection requests.
    Retrieves text from request args, calls emotion_detector,
    and returns formatted response or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    output = emotion_detector(text_to_analyze)

    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions_str = ', '.join(f"'{k}': {v}" for k, v in output.items() if k != 'dominant_emotion')
    return f"For the given statement, the system response is {emotions_str}. \
    The dominant emotion is {output['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
    Render the main index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on host 0.0.0.0 and port 5000 with debug enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
