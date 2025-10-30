import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found! Please add GEMINI_API_KEY to .env")

# Configure Gemini
genai.configure(api_key=api_key)

# Model setup
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_gift_suggestions(data: dict):
    """
    Generate real AI-based gift suggestions using Google Gemini.
    """
    # Create a prompt based on user data
    prompt = f"""
    You are Gifty, an expert AI gift recommender.
    Based on the details below, suggest 3 personalized, realistic, thoughtful gifts.

    ---
    Occasion: {data.get('occasion')}
    For: {data.get('person')}
    Age: {data.get('age')}
    Gender: {data.get('gender')}
    Interests: {data.get('interests')}
    Category: {data.get('category')}
    Style: {data.get('style')}
    Price Range: {data.get('price')}
    Preferred Color: {data.get('color')}
    Additional Notes: {data.get('notes')}
    ---

    Each gift suggestion should be 2-3 sentences, with creative and personal reasoning.
    Format response in clean HTML (<h3>Title</h3><p>Description</p>).
    """

    try:
        response = model.generate_content(prompt)
        return [response.text]
    except Exception as e:
        return [f"<p><strong>Error generating suggestions:</strong> {str(e)}</p>"]
