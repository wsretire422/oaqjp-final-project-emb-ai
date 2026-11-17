import requests, json, math

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the response from the API to json
    formatted_response = json.loads(response.text)

    # Extract the required set of emotions from the formatted_response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the highest score from the set of emotions
    highest_score = max(emotions.values())
    
    # Get the emotion with the highest score
    emotion = [(key, value) for key, value in emotions.items() if value == highest_score]

    # Add the emotion the  with the highest score to response dictionary
    # under 'dominant_emotion' key
    emotions['dominant_emotion'] = emotion[0][0]

    # Return the modified response from the API
    return emotions
