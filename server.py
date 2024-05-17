from flask import Flask, render_template, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = str(request.args.text_to_analyze)

    response = emotion_detector(text_to_analyze)
    format_response = jsonify(emotion_predictor(response))
    return format_response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
