from transformers import pipeline
from pathlib import Path
import json


# Load transformer-based sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)


def analyze_sentiment_and_intent(patient_text):
    """
    Detect patient sentiment and intent from text.
    Uses Transformer inference + clinical interpretation.
    """

    # ---- SENTIMENT (MODEL-DRIVEN) ----
    model_output = sentiment_model(patient_text[:512])[0]
    label = model_output["label"]
    score = model_output["score"]

    # Map generic sentiment to clinical sentiment
    if label == "NEGATIVE" and score > 0.6:
        sentiment = "Anxious"
    elif label == "POSITIVE" and score > 0.6:
        sentiment = "Reassured"
    else:
        sentiment = "Neutral"

    # ---- INTENT (LIGHT NLP LOGIC) ----
    text_lower = patient_text.lower()

    if any(phrase in text_lower for phrase in ["do i need to worry", "will this affect", "long term"]):
        intent = "Seeking reassurance"
    elif any(word in text_lower for word in ["pain", "discomfort", "ache"]):
        intent = "Reporting symptoms"
    elif any(word in text_lower for word in ["thank", "appreciate", "relief"]):
        intent = "Expressing gratitude"
    else:
        intent = "General information"

    return {
        "Sentiment": sentiment,
        "Intent": intent,
        "Model_Confidence": round(score, 3)
    }


def main():
    # Example patient dialogue from conversation
    patient_text = (
        "That’s great to hear. So, I don’t need to worry about this affecting me in the future?"
    )

    result = analyze_sentiment_and_intent(patient_text)

    Path("outputs").mkdir(exist_ok=True)

    with open("outputs/task2_sentiment_intent.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("Sentiment and intent analysis completed and saved.")


if __name__ == "__main__":
    main()
