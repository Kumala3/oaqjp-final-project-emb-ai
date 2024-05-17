import requests
from json import loads, dumps


def emotion_detector(text_to_analyse: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}
    try:
        response = requests.post(url=url, json=data, headers=headers)

        if response.status_code == 200:
            return response.text
        elif response.status_code == 400:
            return dumps(
                {
                    "anger": None,
                    "disgust": None,
                    "fear": None,
                    "joy": None,
                    "sadness": None,
                    "dominant_emotion": None,
                }
            )
        else:
            return dumps({"error": "Server Error"})
    except Exception as e:
        return dumps({"error": "Server Error"})


def emotion_predictor(response):
    json_res = loads(response)
    emotions = json_res["emotionPredictions"][0]["emotion"]

    highest_emotion = next(
        (emotion, score)
        for emotion, score in emotions.items()
        if score == max(emotions.values())
    )

    emotions["dominant_emotion"] = highest_emotion[0]
    return emotions
