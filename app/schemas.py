from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class LeadInput(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    company: str = Field(..., min_length=2)
    lead_id: str


class EnrichResponse(BaseModel):
    linkedin_url: str
    company_size: str
    industry: str
    lead_id: str

class ClassifyInput(BaseModel):
    message: str = Field(..., min_length=3)
    lead_id: str


class ClassifyResponse(BaseModel):
    intent: str
    confidence: float
    reason: Optional[str] = None
    lead_id: str