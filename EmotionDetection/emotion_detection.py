import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP EmotionPredict API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for anger, disgust, fear, joy, sadness, 
              and the dominant emotion.
    """
    # API URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input JSON
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Sending POST request to Watson NLP EmotionPredict API
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Convert the response to a dictionary
        response_data = response.json()

        # Extract emotions
        emotions = response_data['emotionPredictions'][0]['emotion']

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Prepare the output dictionary
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the emotion detection process: {e}")
        return None

# Example usage
if __name__ == "__main__":
    text_to_analyze = "I'm so thrilled to be working on this exciting project!"
    detected_emotions = emotion_detector(text_to_analyze)
    if detected_emotions:
        print("Detected Emotions:")
        print(json.dumps(detected_emotions, indent=2))
