from google import genai
from google.genai import types
import re 
import os
from dotenv import load_dotenv

# API KEY HIDE
load_dotenv()
api_key = os.getenv("API_KEY")

sys_instructions = "You are a scam detection expert. Analyze the given text for scam indicators such as suspicious keywords," \
"fraudulent patterns, emotional manipulation, urgency, or impersonation of trusted entities. Provide a scam likelihood percentage (0-100%)" \
" along with a short reasoning sentence explaining why this message may or may not be a scam, along with atleast 3 keywords if found."

def ai_analysis(suspicious_text):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model = "gemini-2.0-flash", 
        contents = [suspicious_text],
        config=types.GenerateContentConfig(
            system_instruction=sys_instructions
        )
    )

    capture_percent = re.findall("\d+", response.text)
    ai_percent = int(capture_percent[0])

    capture_reasoning = re.search(r"\*\*Reasoning:\*\* (.+)", response.text)
    text_reasoning = capture_reasoning.group(1)

    capture_keywords = re.search(r"\*\*Keywords:\*\* (.+)", response.text, re.DOTALL)
    ai_keywords = capture_keywords.group(1)
    list_form = ai_keywords.split(',')
    # In case of new line characters 
    cleaned_list = [keyword.strip() for keyword in list_form]

    return ai_percent, text_reasoning, cleaned_list
