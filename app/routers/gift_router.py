# app/routers/gift_router.py
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.gift_ai import generate_gift_suggestions

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/manual", response_class=HTMLResponse)
def get_manual_form(request: Request):
    return templates.TemplateResponse("manual.html", {"request": request})

@router.post("/manual", response_class=HTMLResponse)
def process_manual_form(
    request: Request,
    occasion: str = Form(...),
    person: str = Form(...),
    age: str = Form(""),
    gender: str = Form(""),
    interests: str = Form(""),
    category: str = Form(""),
    style: str = Form(""),
    price: str = Form(""),
    color: str = Form(""),
    notes: str = Form("")
):
    # Generate suggestions using AI
    suggestions = generate_gift_suggestions({
        "occasion": occasion,
        "person": person,
        "age": age,
        "gender": gender,
        "interests": interests,
        "category": category,
        "style": style,
        "price": price,
        "color": color,
        "notes": notes
    })
    return templates.TemplateResponse("manual_results.html", {
        "request": request,
        "suggestions": suggestions
    })
