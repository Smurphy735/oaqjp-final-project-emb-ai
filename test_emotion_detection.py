from EmotionDetection.emotion_detection import emotion_detector # Import the function from the package
import unittest # Import the unit test library

# Create the unit test class TestEmotionDetector
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        print("Dominant emotion for joy test:", result_1['dominant_emotion'])
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        print("Dominant emotion for anger test:", result_2['dominant_emotion'])
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        print("Dominant emotion for disgust test:", result_3['dominant_emotion'])
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        print("Dominant emotion for sadness test:", result_4['dominant_emotion'])
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        print("Dominant emotion for fear test:", result_5['dominant_emotion'])
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()