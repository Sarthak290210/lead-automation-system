def enrich_lead_data(name: str, email: str, company: str, lead_id: str):
    name_slug = name.lower().replace(" ", "-")
    company_lower = company.lower()

    if "tech" in company_lower or "software" in company_lower:
        industry = "Technology"
        company_size = "51-200"
    elif "finance" in company_lower:
        industry = "Finance"
        company_size = "201-500"
    else:
        industry = "General Business"
        company_size = "11-50"

    return {
        "linkedin_url": f"https://linkedin.com/in/{name_slug}",
        "company_size": company_size,
        "industry": industry,
        "lead_id" : lead_id
    }