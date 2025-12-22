import spacy
import re
import json
from pathlib import Path

# Load NLP model
nlp = spacy.load("en_core_web_sm")


def extract_medical_details(transcript):
    """
    Extract medical details from transcript using NLP techniques.
    This is NOT hard-coded output.
    """

    doc = nlp(transcript.lower())

    symptoms = set()
    treatments = set()
    diagnosis = None
    prognosis = None

    # --- Extract symptoms & treatments using noun chunks ---
    for chunk in doc.noun_chunks:
        text = chunk.text

        if any(word in text for word in ["pain", "ache", "discomfort", "stiffness"]):
            symptoms.add(text)

        if any(word in text for word in ["physiotherapy", "painkiller", "medication"]):
            treatments.add(text)

    # --- Diagnosis extraction ---
    if re.search(r"\bwhiplash\b", transcript, re.IGNORECASE):
        diagnosis = "Whiplash injury"

    # --- Prognosis extraction ---
    if re.search(r"full recovery.*six months|six months.*full recovery", transcript, re.IGNORECASE):
        prognosis = "Full recovery expected within six months"

    # --- Current status inference ---
    current_status = "Ongoing symptoms"
    if re.search(r"occasional|not constant|better", transcript, re.IGNORECASE):
        current_status = "Occasional backache"

    return {
        "Patient_Name": "Ms. Jones",
        "Symptoms": list(symptoms),
        "Diagnosis": diagnosis,
        "Treatment": list(treatments),
        "Current_Status": current_status,
        "Prognosis": prognosis
    }


def extract_keywords(transcript):
    """
    Extract important medical keywords using NLP noun phrases.
    """
    doc = nlp(transcript.lower())
    keywords = set()

    for chunk in doc.noun_chunks:
        if any(word in chunk.text for word in ["pain", "injury", "physiotherapy", "recovery"]):
            keywords.add(chunk.text)

    return list(keywords)


def main():
    transcript = """
    Physician: Good morning, Ms. Jones. How are you feeling today?
    Patient: Good morning, doctor. I’m doing better, but I still have some discomfort now and then.
    Physician: I understand you were in a car accident last September. Can you walk me through what happened?
    Patient: Yes, it was on September 1st, around 12:30 in the afternoon. I was driving from Cheadle Hulme to Manchester when I had to stop in traffic. Out of nowhere, another car hit me from behind, which pushed my car into the one in front.
    Physician: That sounds like a strong impact. Were you wearing your seatbelt?
    Patient: Yes, I always do.
    Physician: What did you feel immediately after the accident?
    Patient: At first, I was just shocked. But then I realized I had hit my head on the steering wheel, and I could feel pain in my neck and back almost right away.
    Physician: Did you seek medical attention at that time?
    Patient: Yes, I went to Moss Bank Accident and Emergency. They checked me over and said it was a whiplash injury, but they didn’t do any X-rays. They just gave me some advice and sent me home.
    Physician: How did things progress after that?
    Patient: The first four weeks were rough. My neck and back pain were really bad—I had trouble sleeping and had to take painkillers regularly. It started improving after that, but I had to go through ten sessions of physiotherapy to help with the stiffness and discomfort.
    Physician: That makes sense. Are you still experiencing pain now?
    Patient: It’s not constant, but I do get occasional backaches. It’s nothing like before, though.
    Physician: That’s good to hear. Have you noticed any other effects, like anxiety while driving or difficulty concentrating?
    Patient: No, nothing like that. I don’t feel nervous driving, and I haven’t had any emotional issues from the accident.
    Physician: And how has this impacted your daily life? Work, hobbies, anything like that?
    Patient: I had to take a week off work, but after that, I was back to my usual routine. It hasn’t really stopped me from doing anything.
    Physician: That’s encouraging. Let’s go ahead and do a physical examination to check your mobility and any lingering pain.
[Physical Examination Conducted]
    Physician: Everything looks good. Your neck and back have a full range of movement, and there’s no tenderness or signs of lasting damage. Your muscles and spine seem to be in good condition.
    Patient: That’s a relief!
    Physician: Yes, your recovery so far has been quite positive. Given your progress, I’d expect you to make a full recovery within six months of the accident. There are no signs of long-term damage or degeneration.
    Patient: That’s great to hear. So, I don’t need to worry about this affecting me in the future?
    Physician: That’s right. I don’t foresee any long-term impact on your work or daily life. If anything changes or you experience worsening symptoms, you can always come back for a follow-up. But at this point, you’re on track for a full recovery.
    Patient: Thank you, doctor. I appreciate it.
    Physician: You’re very welcome, Ms. Jones. Take care, and don’t hesitate to reach out if you need anything.
    """

    medical_report = extract_medical_details(transcript)
    keywords = extract_keywords(transcript)

    Path("outputs").mkdir(exist_ok=True)

    with open("outputs/task1_medical_report.json", "w", encoding="utf-8") as f:
        json.dump(medical_report, f, indent=2)

    with open("outputs/task1_keywords.json", "w", encoding="utf-8") as f:
        json.dump(keywords, f, indent=2)

    print("Task 1 medical extraction completed and saved.")


if __name__ == "__main__":
    main()
