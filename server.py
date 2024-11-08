"""
Flask application for detecting emotions in text inputs.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """
    Process a text input and return emotion scores and the dominant emotion.
    """
    data = request.json

    # Check if the input is missing or the 'statement' is blank
    if not data or not data.get('statement') or not data['statement'].strip():
        return jsonify({
            "original_statement": None,
            "emotion_scores": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            },
            "response": "Invalid text! Please try again!"
        }), 400

    # Example emotions (mock data)
    statement = data['statement']
    emotions = {
        "anger": 0.006274985,
        "disgust": 0.0025598293,
        "fear": 0.009251528,
        "joy": 0.9680386,
        "sadness": 0.049744144
    }

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get) if all(emotions.values()) else None
    if dominant_emotion is None:
        return jsonify({
            "original_statement": statement,
            "emotion_scores": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            },
            "response": "Invalid text! Please try again!"
        }), 400

    emotions['dominant_emotion'] = dominant_emotion

    # Format response
    formatted_response = "For the given statement, the system response is "
    formatted_response += ", ".join(
        [f"'{key}': {value}" for key, value in emotions.items() if key != "dominant_emotion"]
    )
    formatted_response += f". The dominant emotion is {dominant_emotion}."

    return jsonify({
        "original_statement": statement,
        "emotion_scores": emotions,
        "response": formatted_response
    }), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
