# Trinethra Module: AI-Assisted Supervisor Feedback Analyzer

### Project Overview
This is a full-stack AI application developed for the DeepThought Software Development Internship. The Trinethra Module is designed to assist psychology interns in analyzing supervisor transcripts by mapping raw human feedback to a structured 1-10 performance rubric.

### Technical Stack
- Frontend/Backend: Streamlit (Python)
- AI Engine: Ollama (Local LLM)
- Model: Llama 3.2
- Data Handling: Python JSON library + String Filtering Guardrails

### Engineering Guardrails and Anti-Hallucination
To ensure the AI remains factual and follows the DeepThought Fellow Model, I implemented the following:

1. Deterministic Setting (Temperature 0.1): I locked the model’s creativity to a near-zero setting. This ensures the scores are based strictly on evidence in the transcript, not AI imagination.
2. Simplified Prompt Engineering: Instead of overwhelming the model with a complex rubric file, I optimized the prompt to focus on the 4 core dimensions (Execution, Systems, KPI, Change Management). This prevents looping and context overflow.
3. Output Guardrail (JSON Cleaner): I built a custom filter in Python to strip away conversational AI chatter and Markdown formatting (backticks). This ensures the application only processes and displays valid, structured JSON.

### Product Thinking and Creativity
- Dynamic Text Input: While the assignment provided samples, I designed the UI with a live text area. This makes the tool future-proof, allowing interns to paste any new transcript from a live call for instant analysis.
- Bias Filtering: The prompt is specifically instructed to ignore Supervisor Presence Bias (e.g., being upset about laptop usage) and look for Layer 2 Systems Building evidence instead.

### Setup Instructions
1. Install Ollama: ollama.com
2. Pull Model: ollama pull llama3.2
3. Install Dependencies: pip install streamlit ollama
4. Run Application: python -m streamlit run main.py

### Repository Structure
- main.py: The full-stack application code.
- rubric.json: The scoring logic.
- sample-transcripts.json: Test data for validation.
- thought-process-sketch.jpg: Hand-drawn architecture and logic flow.

### Final Note
This project demonstrates the ability to integrate local LLMs into a functional business tool while maintaining high data integrity and user-centric design.
