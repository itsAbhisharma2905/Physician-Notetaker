Medical NLP Pipeline – Physician–Patient Conversation Analysis
📌 Overview

This project implements an end-to-end NLP pipeline to analyze physician–patient conversations and extract structured medical insights.
It covers medical entity extraction, patient sentiment and intent analysis, and automated SOAP note generation, following real-world healthcare NLP practices.

The solution uses spaCy for medical text processing and Transformer-based models (DistilBERT) for sentiment analysis.

✅ Tasks Implemented
Task 1: Medical NLP Extraction

NLP-based extraction of:

Symptoms

Diagnosis

Treatment

Prognosis

Structured medical summary generation

Keyword extraction of important medical phrases

Task 2: Sentiment & Intent Analysis

Transformer-based sentiment classification:

Anxious

Neutral

Reassured

Patient intent detection:

Reporting symptoms

Seeking reassurance

Expressing concern or gratitude

Task 3: SOAP Note Generation (Bonus)

Automated conversion of transcripts into SOAP notes

Logical mapping of:

Subjective

Objective

Assessment

Plan

Clinically readable, EHR-style output

📁 Project Structure
medical_nlp_pipeline/
│
├── data/
│   └── conversation.txt          # Input physician–patient transcript
│
├── src/
│            
│   ├── task1_medical_nlp.py      # Medical entity extraction & keywords
│   ├── task2_sentiment_intent.py # Sentiment & intent analysis
│   ├── task3_soap_generator.py   # SOAP note generation
│
├── outputs/
│   ├── task1_medical_report.json
│   ├── task1_keywords.json
│   ├── task2_sentiment_intent.json
│   └── task3_soap_note.json
│
|                
├── requirements.txt
└── README.md

🛠️ Setup Instructions
🔹 Prerequisites

Python 3.8 or higher

pip installed

🔹 (Recommended) Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


Mac / Linux

python3 -m venv venv
source venv/bin/activate

🔹 Install Dependencies
pip install -r requirements.txt

🔹 Download spaCy Language Model
python -m spacy download en_core_web_sm


(This is required for medical NER and keyword extraction.)

▶️ How to Run the Project

From the project root directory:

python main.py

📤 Output Files

After execution, the following files are automatically generated in the outputs/ folder:

File Name	Description
task1_medical_report.json	Structured medical summary
task1_keywords.json	Extracted medical keywords
task2_sentiment_intent.json	Patient sentiment & intent
task3_soap_note.json	Generated SOAP note
🧠 Design Highlights

NLP-driven extraction (no hard-coded outputs)

Transformer-based sentiment analysis

Hybrid rule + NLP approach for clinical safety

Modular and readable code structure

Outputs suitable for downstream healthcare systems

👤 Author

Abhi Sharma
Medical NLP Assignment Submission