''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the list of emotions and its dominant 
        emotion for the provided text.
    '''
    text=request.args.get('textToAnalyze')
    emotion=emotion_detector(text)
    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    labels = ("anger", "disgust", "fear", "joy", "sadness")

    scores = [f"'{label}': {emotion[label]}" for label in labels]
    scores_text = ", ".join(scores[:-1]) + " and " + scores[-1]

    return (
        f"For the given statement, the system response is {scores_text}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
    )

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
