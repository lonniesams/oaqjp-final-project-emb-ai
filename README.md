
# **Emotion Detector Flask Application**

This project is a Flask-based web application that analyzes a given text input to detect emotions and identify the dominant emotion. It returns a JSON response containing the emotion scores and a formatted message describing the result.

---

## **Features**
- Accepts a text statement via a POST request.
- Returns emotion scores for anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Handles invalid inputs and blank entries gracefully.

---

## **Technologies Used**
- **Python 3.8+**
- **Flask**: Lightweight web framework for building the API.
- **PyLint**: For static code analysis and maintaining high code quality.

---

## **Setup Instructions**

### **Prerequisites**
1. **Python**: Ensure Python is installed on your system. Check using:
   ```bash
   python --version
   ```
2. **Pip**: Ensure pip is installed. Check using:
   ```bash
   pip --version
   ```

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/emotion-detector.git
   cd emotion-detector
   ```
2. Install the required Python packages:
   ```bash
   pip install flask pylint
   ```

3. Verify the setup:
   ```bash
   pylint server.py
   ```
   Ensure a score of **10/10** is achieved.

---

## **Usage**

### **Running the Application**
Start the Flask server:
```bash
python server.py
```
You should see output similar to:
```
 * Running on http://127.0.0.1:5000
```

### **Testing the Application**
#### **Using Postman**
1. Open Postman.
2. Create a new **POST** request with the following details:
   - **URL**: `http://127.0.0.1:5000/emotionDetector`
   - **Headers**: `Content-Type: application/json`
   - **Body** (raw JSON):
     ```json
     {
         "statement": "I love my life"
     }
     ```
3. Send the request. You should receive a JSON response with the emotion scores and the dominant emotion.

#### **Using cURL**
Run the following command in your terminal:
```bash
curl -X POST http://127.0.0.1:5000/emotionDetector -H "Content-Type: application/json" -d "{\"statement\": \"I love my life\"}"
```

#### **Expected Response**
```json
{
    "original_statement": "I love my life",
    "emotion_scores": {
        "anger": 0.006274985,
        "disgust": 0.0025598293,
        "fear": 0.009251528,
        "joy": 0.9680386,
        "sadness": 0.049744144,
        "dominant_emotion": "joy"
    },
    "response": "For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386, 'sadness': 0.049744144. The dominant emotion is joy."
}
```

---

## **Error Handling**

### **Invalid Input**
If the input is missing or empty, the API returns:
- **Status Code**: `400`
- **Response**:
  ```json
  {
      "original_statement": null,
      "emotion_scores": {
          "anger": null,
          "disgust": null,
          "fear": null,
          "joy": null,
          "sadness": null,
          "dominant_emotion": null
      },
      "response": "Invalid text! Please try again!"
  }
  ```

---

## **Project Structure**
```
emotion-detector/
│
├── server.py           # Main application file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## **Future Enhancements**
- Integrate a machine learning model to analyze text and generate real-time emotion scores.
- Create a user-friendly front-end interface.
- Deploy the application on a cloud platform like Heroku, AWS, or Google Cloud.

---

## **License**
This project is licensed under the [MIT License](LICENSE).
