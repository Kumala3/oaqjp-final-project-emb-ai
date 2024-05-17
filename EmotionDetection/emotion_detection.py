import requests
from json import loads, dumps


def emotion_detector(text_to_analyse: str):
    """
    Detects the emotion in the given text using a remote API.

    Args:
        text_to_analyse (str): The text to be analyzed for emotion detection.

    Returns:
        str: The response from the emotion detection API. If the API call is successful, the response will contain the detected emotions. If the API call fails, the response will contain an error message.
    """
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
    except Exception:
        return dumps({"error": "Server Error"})


def emotion_predictor(response: dict):
    """
    Predicts the dominant emotion from the given response.

    Args:
        response (dict): A dictionary containing the response data.

    Returns:
        dict: A dictionary containing the emotions and the dominant emotion.
    """
    json_res = loads(response)
    emotions = json_res["emotionPredictions"][0]["emotion"]

    highest_emotion = next(
        (emotion, score)
        for emotion, score in emotions.items()
        if score == max(emotions.values())
    )

    emotions["dominant_emotion"] = highest_emotion[0]
    return emotions
