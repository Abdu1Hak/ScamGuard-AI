from google import genai
from google.genai import types
import re 
import os
from dotenv import load_dotenv
import json 

# API KEY HIDE
load_dotenv()
api_key = os.getenv("API_KEY")

sys_instructions = """You are a scam detection expert. Analyze the given text for scam indicators such as suspicious keywords,
fraudulent patterns, emotional manipulation, urgency, or impersonation of trusted entities. Provide a scam likelihood percentage (0-100%)
along with a short reasoning sentence explaining why this message may or may not be a scam, along with atleast 3 keywords if found.
You must respond only in a JSON object, nothing else, following this schema:"

{
  "likelihood": <integer 0 to 100>,
  "reasoning": "<string>",
  "keywords": [ "<string>", "<string>", "<string>" ]
}
"""


# suspicious_text = "Dear Valued Customer"\
# "We have detected suspicious activity on your account, and for your safety, we have temporarily suspended access" \
# "To restore your account, please verify your information immediately by clicking the secure link below" \
# "👉 Click Here to Restore Access"\
# "Failure to comply within 24 hours will result in permanent deactivation of your account."\
# "Thank you for your prompt attention to this matter." 

def ai_analysis(suspicious_text):
    client   = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[suspicious_text],
        config=types.GenerateContentConfig(system_instruction=sys_instructions)
    )

    print("=== RAW RESPONSE ===")
    print(response.text)
    print("====================")

    m = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", response.text, flags=re.DOTALL)
    json_payload = m.group(1) if m else response.text
    
    data = json.loads(json_payload)
    ai_percent = data["likelihood"]
    ai_reasoning = data["reasoning"]
    ai_keywords = data["keywords"]
    return ai_percent, ai_reasoning, ai_keywords


    # m = re.search(r"\*\*Scam Likelihood:\*\*\s*(\d+)%", raw)
    # ai_percent = int(m.group(1))

    # # ── 2) Reasoning ────────────────────────────────────────────────────────────
    # #    We allow any text until the next **Keywords:** header
    # m = re.search(
    #     r"\*\*Reasoning:\*\*\s*(.+?)(?=\r?\n\*\*Keywords:\*\*)",
    #     raw,
    #     flags=re.DOTALL
    # )
    # ai_reasoning = m.group(1).strip() if m else "(no reasoning found)"

    # # ── 3) Keywords ─────────────────────────────────────────────────────────────
    # #    Capture everything after **Keywords:** (skip blank lines), then grab each '* …' line
    # m = re.search(r"\*\*Keywords:\*\*\s*(.+)", raw, flags=re.DOTALL)
    # if not m:
    #     ai_keywords = []
    # else:
    #     block = m.group(1).strip()

    #     # a) If it's a bullet list, each line starts with "*"
    #     if block.lstrip().startswith("*"):
    #         items = re.findall(r"^\s*\*\s*(.+?)\s*$", block, flags=re.MULTILINE)
    #     else:
    #         # b) Otherwise assume inline quoted items separated by commas
    #         #    Extract what's inside each pair of quotes
    #         items = re.findall(r'"([^"]+)"', block)

    #     # clean trailing punctuation and wrap in quotes
    #     ai_keywords = [f'"{item.rstrip(".,").strip()}"' for item in items]

    # return ai_percent, ai_reasoning, ai_keywords
    

