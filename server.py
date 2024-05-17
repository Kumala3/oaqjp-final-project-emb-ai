"""
Server module for emotion detection application using Flask.
"""

from flask import Flask, render_template, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint for detecting emotions in text.

    Returns:
        A JSON response containing the formatted emotion prediction or an error message.

    """
    text_to_analyze = str(request.args.get("textToAnalyze"))

    if not text_to_analyze:
        return jsonify("Invalid text! Please try again!"), 422

    response = emotion_detector(text_to_analyze)
    format_response = emotion_predictor(response)

    if format_response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!."}, 400)

    return format_response, 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
