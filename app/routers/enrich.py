from fastapi import APIRouter, HTTPException
from app.schemas import LeadInput, EnrichResponse
from app.services.enrichment_system import enrich_lead_data

router = APIRouter()


@router.post("/enrich", response_model=EnrichResponse)
def enrich_lead(lead: LeadInput):
    try:
        return enrich_lead_data(
            name=lead.name,
            email=lead.email,
            company=lead.company,
            lead_id = lead.lead_id
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Enrichment failed: {str(e)}"
        )