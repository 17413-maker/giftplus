from fastapi import APIRouter, Form
from app.utils.email_sender import send_verification_email
import random

auth_router = APIRouter()
verification_codes = {}  # temporary in-memory store

# Send verification code
@auth_router.post("/send_verification")
def send_verification(email: str = Form(...)):
    code = str(random.randint(100000, 999999))  # generate 6-digit code
    if send_verification_email(email, code):
        verification_codes[email] = code
        return {"message": "Verification email sent!"}
    else:
        return {"detail": "Failed to send email"}

# Verify code
@auth_router.post("/verify_code")
def verify_code(email: str = Form(...), code: str = Form(...)):
    stored_code = verification_codes.get(email)
    if not stored_code:
        return {"detail": "No code found for this email"}
    if stored_code != code:
        return {"detail": "Invalid code"}
    # Success
    del verification_codes[email]  # remove code after verification
    return {"message": "Email verified successfully!"}
