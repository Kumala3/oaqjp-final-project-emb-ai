import requests
from json import loads


def emotion_detector(text_to_analyse: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url=url, json=data, headers=headers)
    return response.text


# {
#     "emotionPredictions": [
#         {
#             "emotion": {
#                 "anger": 0.0075737,
#                 "disgust": 0.0022305858,
#                 "fear": 0.01696498,
#                 "joy": 0.9918238,
#                 "sadness": 0.018872749,
#             },
#             "target": "",
#             "emotionMentions": [
#                 {
#                     "span": {"begin": 0, "end": 24, "text": "I love new technologies!"},
#                     "emotion": {
#                         "anger": 0.0075737,
#                         "disgust": 0.0022305858,
#                         "fear": 0.01696498,
#                         "joy": 0.9918238,
#                         "sadness": 0.018872749,
#                     },
#                 }
#             ],
#         }
#     ],
#     "producerId": {"name": "Ensemble Aggregated Emotion Workflow", "version": "0.0.1"},
# }


def format_output(response):
    json_res = loads(response)
    emotions = json_res["emotionPredictions"][0]["emotion"]
    
    emotions_list = []

    for emotion in emotions.values():
        emotions_list.append(emotion)

    return max(emotions_list)


if __name__ == "__main__":
    text = "I hate AI because it will replace real people jobs!"

    result = emotion_detector(text)
    print(format_output(result))
