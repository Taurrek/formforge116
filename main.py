from fastapi import FastAPI
from backend_upload_bundle import app as upload_app
from backend_email import app as email_app

app = FastAPI()
# Mount at the exact paths your frontend expects
app.mount("/api/upload-bundle/", upload_app)
app.mount("/api/send-report-email/", email_app)
