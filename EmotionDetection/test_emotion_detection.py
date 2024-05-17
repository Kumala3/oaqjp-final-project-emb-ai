import unittest

from EmotionDetection import emotion_predictor, emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        response = emotion_detector(text)
        result = emotion_predictor(response)["dominant_emotion"]
        self.assertEqual(result, "joy")
