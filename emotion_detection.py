import requests


def emotion_detector(text_to_analyse: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url=url, json=data, headers=headers)
    return response.text


if __name__ == "__main__":
    text = "I love new technologies!"

    result = emotion_detector(text)
    print(result)
