import streamlit as st
import ollama
import json

st.set_page_config(page_title="Trinethra AI Analyzer", layout="wide")
st.title("Trinethra: Supervisor Feedback Analyzer")

try:
    with open('rubric.json', 'r') as f:
        rubric_data = json.load(f)
    with open('sample-transcripts.json', 'r') as f:
        transcripts_data = json.load(f)
except Exception as e:
    st.error(f"Error loading files: {e}. Make sure rubric.json and sample-transcripts.json are in this folder!")

st.sidebar.header("Input Data")
transcript_input = st.sidebar.text_area("Paste Supervisor Transcript here:", height=300)

if st.sidebar.button("Analyze Transcript"):
    if not transcript_input:
        st.warning("Please paste a transcript!")
    else:
        with st.spinner("AI is analyzing..."):
            prompt = f"""
            Analyze the following transcript based on these 4 categories: 
            1. Driving Execution
            2. Building Systems
            3. KPI Impact
            4. Change Management

            For each category, give a score (1-10) and a brief reason.
            TRANSCRIPT: {transcript_input}

            OUTPUT FORMAT:
            Respond ONLY with a JSON object like this:
            {{"execution": {{"score": 0, "reason": ""}}, "systems": {{"score": 0, "reason": ""}}}}
            """
            
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': prompt}
            ], options={'temperature': 0.1})
            
            raw_content = response['message']['content']

            try:
                clean_json = raw_content.strip()
                if "```json" in clean_json:
                    clean_json = clean_json.split("```json")[1].split("```")[0].strip()
                
                analysis = json.loads(clean_json)
                st.subheader("Analysis Result")
                st.json(analysis)
            except Exception:
                st.error(" AI gave an invalid response. Try clicking Analyze again.")
                with st.expander("See Raw AI Output"):
                    st.text(raw_content)   
            st.success("Analysis Complete! You can now review and edit these findings.")