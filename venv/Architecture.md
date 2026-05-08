**Final Flow**

Lead Form / Postman

↓

n8n Webhook

↓

Validate Input

↓

FastAPI /enrich

↓

FastAPI /classify using OpenAI LLM

↓

Google Sheets / Airtable / DB

↓

Slack / Email Notification



**Build Order**

1\. Created FastAPI app(Backend)

2\. Add /enrich

3\. Add OpenAI /classify

4\. Test in Postman

5\. Create n8n webhook

6\. Add validation

7\. Add lead_id

8\. Call /enrich

9\. Call /classify

10\. Store in Google Sheets

11\. Send notification(Email for confirmation of new lead_id added)

12\. Test full flow from Postman

13\. Export n8n workflow JSON