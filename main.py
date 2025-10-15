from fastapi import FastAPI
from app.routers import auth_router

app = FastAPI(title="Aditya OSINT App")

# Include auth router
app.include_router(auth_router.auth_router, prefix="/auth", tags=["Auth"])

# Health check
@app.get("/")
def root():
    return {"message": "Aditya OSINT Backend Running"}
