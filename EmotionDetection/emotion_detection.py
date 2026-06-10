import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(url, json=myobj, headers=header)
    
    print(f"HTTP Status Code: {response.status_code}")  # Debug print

    if response.status_code == 400:
        # Return dictionary with all values as "none"
        return {
            'anger': "none",
            'disgust': "none",
            'fear': "none",
            'joy': "none",
            'sadness': "none",
            'dominant_emotion': None
        }

    response.raise_for_status()  # Raise error for other bad statuses

    data = json.loads(response.text)
    emotions = data['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return output