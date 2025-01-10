import requests
import json

def emotion_detector(text):
    text_to_analyze = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = float(formatted_response["emotionPredictions"][0]["emotion"]["anger"])
        disgust_score = float(formatted_response["emotionPredictions"][0]["emotion"]["disgust"])
        fear_score = float(formatted_response["emotionPredictions"][0]["emotion"]["fear"])
        joy_score = float(formatted_response["emotionPredictions"][0]["emotion"]["joy"])
        sadness_score = float(formatted_response["emotionPredictions"][0]["emotion"]["sadness"])
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
    
    emotion_dict = {
        'anger': anger_score, 
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }
    
    if all(value is None for value in emotion_dict.values()):
        emotion_dict['dominant_emotion'] = None  # No dominant emotion
    else:
        dominant_emotion = max(
        {k: v for k, v in emotion_dict.items() if v is not None},
        key=lambda x: emotion_dict[x])
        emotion_dict['dominant_emotion'] = dominant_emotion

  
    return  emotion_dict