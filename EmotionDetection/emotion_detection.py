import requests
import json

def emotion_detector(text):
    text_to_analyze = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    anger_score = float(formatted_response["emotionPredictions"][0]["emotion"]["anger"])
    disgust_score = float(formatted_response["emotionPredictions"][0]["emotion"]["disgust"])
    fear_score = float(formatted_response["emotionPredictions"][0]["emotion"]["fear"])
    joy_score = float(formatted_response["emotionPredictions"][0]["emotion"]["joy"])
    sadness_score = float(formatted_response["emotionPredictions"][0]["emotion"]["sadness"])
    emotion_dict = {
        'anger': anger_score, 
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }

    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion

  
    return  emotion_dict