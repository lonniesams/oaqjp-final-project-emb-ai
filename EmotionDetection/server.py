from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    # Simulating an emotion detection process
    statement = request.json.get('statement', '')
    
    # Placeholder emotion detection results (mock data)
    emotions = {
        "anger": 0.006274985,
        "disgust": 0.0025598293,
        "fear": 0.009251528,
        "joy": 0.9680386,
        "sadness": 0.049744144
    }
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    # Format response
    formatted_response = f"For the given statement, the system response is "
    formatted_response += ", ".join([f"'{k}': {v}" for k, v in emotions.items() if k != "dominant_emotion"])
    formatted_response += f". The dominant emotion is {dominant_emotion}."
    
    return jsonify({
        "original_statement": statement,
        "emotion_scores": emotions,
        "response": formatted_response
    }), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
