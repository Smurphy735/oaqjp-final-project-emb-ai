# Import the relevant libraries and functions
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app by the name Emotion Detector
app = Flask(__name__)

# Define the function
@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    output = emotion_detector(text_to_analyze)
    
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response string using the returned dictionary
    emotions_str = ', '.join(f"'{k}': {v}" for k, v in output.items() if k != 'dominant_emotion')
    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {output['dominant_emotion']}."

#run the render_template function on the HTML template index.html
@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

#run the application on host: 0.0.0.0 (or localhost) on port number 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)