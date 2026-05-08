import json
from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def classify_lead_intent(message: str):
    prompt = f"""
You are an AI assistant for a lead automation system.

Classify the user's lead message into exactly one of these intents:

1. sales_enquiry
2. pricing_request
3. support_request
4. partnership_request
5. job_request
6. spam
7. unknown

Rules:
- If the user shows interest in services, classify as sales_enquiry.
- If the user asks about price, cost, plan, quote, or budget, classify as pricing_request.
- If the user needs help with an existing product or service, classify as support_request.
- If the user wants collaboration, classify as partnership_request.
- If the user asks for job/internship, classify as job_request.
- If message is irrelevant or promotional, classify as spam.
- If unclear, classify as unknown with low confidence.

Return only valid JSON in this format:
{{
  "intent": "sales_enquiry",
  "confidence": 0.92,
  "reason": "The user is interested in services."
}}

User message:
{message}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    output_text = response.output_text

    try:
        result = json.loads(output_text)
        return result

    except json.JSONDecodeError:
        return {
            "intent": "unknown",
            "confidence": 0.30,
            "reason": "Could not parse LLM response clearly."
        }