# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import os

# -------------------------------
# CONFIGURATION
# -------------------------------
app = FastAPI()

# Mount directories
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Set your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")  # ← Paste your key here

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------------
# ROUTES
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/manual", response_class=HTMLResponse)
async def manual_mode(request: Request):
    return templates.TemplateResponse("manual.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate_gift(
    request: Request,
    person: str = Form(...),
    age: str = Form(""),
    gender: str = Form(""),
    interests: str = Form(""),
    category: str = Form(""),
    style: str = Form(""),
    price: str = Form(""),
    color: str = Form(""),
    notes: str = Form(""),
    occasion: str = Form("")
):
    # -------------------------------
    # AI PROMPT for Gemini
    # -------------------------------
    prompt = f"""
    You are a creative AI gift recommendation assistant.
    Suggest 5 unique and thoughtful gifts for the following person.

    Person: {person}
    Age: {age}
    Gender: {gender}
    Interests: {interests}
    Gift category: {category}
    Style: {style}
    Price range: {price} INR
    Favorite color: {color}
    Notes: {notes}
    Occasion: {occasion}

    Return the answer in a numbered list with short and creative descriptions.
    """

    try:
        response = model.generate_content(prompt)
        ai_output = response.text
    except Exception as e:
        ai_output = f"⚠️ Gemini Error: {str(e)}"

    return templates.TemplateResponse(
        "manual.html",
        {"request": request, "suggestions": ai_output, "person": person, "occasion": occasion},
    )


@app.get("/health")
async def health_check():
    return {"status": "online", "message": "Gemini-powered Aditya OSINT gift engine ready ✅"}
