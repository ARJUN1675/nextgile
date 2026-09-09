from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Nexgile WealthAgent API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/auth/login")
def login(credentials: LoginRequest):
    if len(credentials.password) < 4:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    name = credentials.email.split("@")[0].replace(".", " ").title()
    return {"token": "demo-session-token", "user": {"name": name, "email": credentials.email, "role": "Individual Client"}}

@app.get("/api/dashboard")
def dashboard():
    return {
        "portfolioValue": 2847650,
        "change": 2.4,
        "allocation": [{"name":"Equities","value":58,"color":"#35d0a1"},{"name":"Fixed income","value":24,"color":"#8299ff"},{"name":"Alternatives","value":12,"color":"#f1b566"},{"name":"Cash","value":6,"color":"#d9e2ed"}],
        "goals": [{"title":"Retirement","progress":76,"target":"$3.75M by 2038"},{"title":"Education fund","progress":62,"target":"$240K by 2031"}],
        "activities": ["Quarterly portfolio review ready", "Tax-loss harvesting opportunity identified", "Beneficiary review due in 18 days"],
    }
