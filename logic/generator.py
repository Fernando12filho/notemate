from openai import OpenAI
import os
from prompts.templates import build_homepage_prompt

client = OpenAI()

def generate_site_content(data):
    prompt = build_homepage_prompt(data)
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {"role": "system", "content": "You are a professional web content writer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.output[0].content[0].text

def transcribe_audio(filepath):
    try:
        audio_file = open(filepath, "rb")
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            response_format="text"
        )
        return transcript
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Transcription failed due to an error."

def generate_summary(text):
    prompt = f"""
    Summarize the following lecture transcript into 3-5 concise bullet points capturing the key highlights:
    {text}
    """
    try:
        response = client.responses.create(
            model="gpt-4.1",
            input=[
                {"role": "system", "content": "You are an educational assistant that generates concise summaries."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.output[0].content[0].text
    except Exception as e:
        print(f"Error during summary generation: {e}")
        return "Summary generation failed due to an error."
    

def generate_quiz(text):
    prompt = f"""
        Based on the following lecture transcript, generate 3 multiple-choice quiz questions with 4 answer options each. Provide the correct answer and a brief explanation for each question.
        Format each question as:
        **Question X:**
        [Question text]
        A) [Option 1]
        B) [Option 2]
        C) [Option 3]
        D) [Option 4]
        **Correct Answer:** [Letter] - [Brief explanation]
        
        Transcript:
        {text}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an educational assistant that creates quiz questions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating quiz: {str(e)}"