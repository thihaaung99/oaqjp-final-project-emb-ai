from flask import FLask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detector():
    input=request.args.get('textToAnalyze')
    emotion=emotion_detector(input)
    labels = ("anger", "disgust", "fear", "joy", "sadness")

    scores = [f"'{label}': {emotion[label]}" for label in labels]
    scores_text = ", ".join(scores[:-1]) + " and " + scores[-1]

    return (
        f"For the given statement, the system response is {scores_text}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
    )
