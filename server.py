from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

@app.router("/emotionDetector")
def emotion_detector():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
