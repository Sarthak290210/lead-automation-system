
## Overview

This project implements a production-oriented lead automation pipeline with the following capabilities:

- **Lead ingestion** via n8n webhook (compatible with any form, Postman, or CRM)
- **Input validation** with idempotency support (deduplication by lead_id)
- **Data enrichment** via a FastAPI `/enrich` endpoint (LinkedIn URL, company size, industry)
- **AI intent classification** via a FastAPI `/classify` endpoint backed by an LLM prompt
- **Structured storage** in Google Sheets / Airtable / database
- **Real-time notifications** via Slack or Email on new lead ingestion

The system is designed to be modular, observable, and scalable — capable of processing 1000+ leads/hour with queue-based async extensions (Celery + Redis).