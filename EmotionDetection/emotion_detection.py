from transformers import pipeline

# Load the local model pipeline once
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def emotion_detector(text_to_analyse):
    """
    Analyze the text and return scores for anger, disgust, fear, joy, and sadness,
    plus the dominant emotion.
    """
    # Get all emotions from the model
    results = emotion_classifier(text_to_analyse)[0]

    # Map the Hugging Face labels to your 5 emotions
    emotion_map = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    for item in results:
        label = item['label'].lower()
        score = item['score']
        if label in emotion_map:
            emotion_map[label] = score

    # Determine dominant emotion
    dominant_emotion = max(emotion_map, key=emotion_map.get)

    # Add dominant_emotion to result
    emotion_map['dominant_emotion'] = dominant_emotion

    return emotion_map
