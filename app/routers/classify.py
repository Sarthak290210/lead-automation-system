from fastapi import APIRouter, HTTPException
from app.schemas import ClassifyInput, ClassifyResponse
from app.services.openai_service import classify_lead_intent

router = APIRouter()


@router.post("/classify", response_model=ClassifyResponse)
def classify_intent(data: ClassifyInput):
    try:
        #result = classify_lead_intent(data.message)
        message = data.message.lower()
        lead_id = data.lead_id.lower()
        if "interested" in message or "service" in message:
            return {"intent": "sales_enquiry", "confidence": 0.92,"reason": "The user is interested in services.","lead_id":lead_id}

        if "price" in message or "cost" in message:
            return {"intent": "pricing_request", "confidence": 0.88,"reason": "The user is interested in services.","lead_id":lead_id}

        if "support" in message or "help" in message:
            return {"intent": "support_request", "confidence": 0.85,"reason": "The user is interested in services.","lead_id":lead_id}

        return {"intent": "unknown", "confidence": 0.45,"reason": "The user might be interested in services.","lead_id":lead_id}
        """return {
            "intent": result.get("intent", "unknown"),
            "confidence": result.get("confidence", 0.0),
            "reason": result.get("reason", "")
        }"""

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Classification failed: {str(e)}"
        )
        