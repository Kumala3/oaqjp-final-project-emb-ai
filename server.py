from flask import Flask, render_template, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = str(request.args.get("textToAnalyze"))

    if not text_to_analyze:
        return jsonify("Invalid text! Please try again!"), 422

    try:
        response = emotion_detector(text_to_analyze)
        format_response = emotion_predictor(response)

        if format_response["dominant_emotion"] is None:
            return jsonify({"error": "Invalid text! Please try again!."}, 400)

        return format_response, 200
    except Exception as e:
        return jsonify({"error": "Server Error"}, 500)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
