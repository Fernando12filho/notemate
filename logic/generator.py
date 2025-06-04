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
