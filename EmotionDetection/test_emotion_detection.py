import unittest

from emotion_detection import emotion_predictor, emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "joy")

    def test_sadness(self):
        text = "I am so sad about this"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "sadness")

    def test_anger(self):
        text = "I am really mad about this"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "anger")

    def test_fear(self):
        text = "I am really afraid that this will happen"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "fear")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "disgust")
