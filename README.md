# Emotion Detector Flask App

This project deploys a simple Flask web application that allows a user to input a text string and analyzes which emotion among a set of 5 is most likely being conveyed.  

Emotions detected:
- anger
- disgust
- fear
- joy
- sadness

The app uses a Hugging Face Transformers model locally to perform emotion classification.

---

## 📦 Project Structure

```
EmotionDetector/
│
├── server.py
├── requirements.txt
├── README.md
└── EmotionDetection/
    └── emotion_detection.py
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd EmotionDetector
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # On Mac/Linux
.venv\Scripts\activate           # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```bash
python server.py
```

By default it runs at:
```
http://localhost:5007
```

### 5️⃣ Use the Emotion Detector

You can test it in your browser or with a URL like:

```bash
http://localhost:5007/emotionDetector?textToAnalyze=I am so happy today!
```

Example response:
```
For the given statement, the system response is
'anger': 0.01, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.93, 'sadness': 0.03.
The dominant emotion is <strong>joy</strong>.
```

---

## 🧭 Notes

✅ No external paid APIs required  
✅ Uses local Hugging Face model: j-hartmann/emotion-english-distilroberta-base  
✅ Internet is needed only once to download the model  

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- Transformers
- Torch

---

## 📜 License

Free to use for educational purposes.