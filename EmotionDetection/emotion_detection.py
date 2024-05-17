import requests
from json import loads


def emotion_detector(text_to_analyse: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url=url, json=data, headers=headers)
    return response.text


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
