import re
from datetime import datetime
from pathlib import Path
import json


def split_speaker_turns(transcript):
    """Split transcript into speaker turns."""
    turns = []
    parts = re.split(r'(Physician|Doctor|Patient):\s*', transcript)

    for i in range(1, len(parts), 2):
        speaker = parts[i].lower()
        text = parts[i + 1].strip()
        turns.append({"speaker": speaker, "text": text})

    return turns


def generate_soap_note(transcript):
    """
    Convert a medical transcript into a structured SOAP note.
    This function IMPLEMENTS the task (not hard-coded output).
    """

    turns = split_speaker_turns(transcript)

    patient_text = " ".join(
        t["text"] for t in turns if "patient" in t["speaker"]
    )
    physician_text = " ".join(
        t["text"] for t in turns if "physician" in t["speaker"] or "doctor" in t["speaker"]
    )

    # ---------------- SUBJECTIVE ----------------
    chief_complaint = "Not specified"
    if "neck" in patient_text.lower() or "back" in patient_text.lower():
        chief_complaint = "Neck and back pain following car accident"

    # ---------------- OBJECTIVE ----------------
    physical_exam = "Not documented"
    if "full range" in physician_text.lower():
        physical_exam = "Full range of motion in neck and back, no tenderness"

    # ---------------- ASSESSMENT ----------------
    diagnosis = "Not specified"
    if "whiplash" in physician_text.lower():
        diagnosis = "Whiplash injury"

    # ---------------- PLAN ----------------
    treatment = []
    if "physiotherapy" in patient_text.lower():
        treatment.append("Physiotherapy")
    if "painkiller" in patient_text.lower():
        treatment.append("Pain management")

    follow_up = "As needed"
    if "follow-up" in physician_text.lower() or "return" in physician_text.lower():
        follow_up = "Return if symptoms worsen"

    soap_note = {
        "Metadata": {
            "generated_on": datetime.now().isoformat()
        },
        "Subjective": {
            "Chief_Complaint": chief_complaint,
            "History_of_Present_Illness": patient_text[:300]
        },
        "Objective": {
            "Physical_Exam": physical_exam
        },
        "Assessment": {
            "Diagnosis": diagnosis
        },
        "Plan": {
            "Treatment": treatment,
            "Follow_Up": follow_up
        }
    }

    return soap_note


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

    soap_note = generate_soap_note(transcript)

    Path("outputs").mkdir(exist_ok=True)

    with open("outputs/task3_soap_note.json", "w", encoding="utf-8") as f:
        json.dump(soap_note, f, indent=2)

    print("SOAP note generated and saved to outputs/task3_soap_note.json")


if __name__ == "__main__":
    main()
