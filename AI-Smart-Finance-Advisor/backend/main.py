from fastapi import FastAPI

from backend.database import create_tables

app = FastAPI()

# ==========================================
# CREATE DATABASE TABLES
# ==========================================

create_tables()

@app.get("/")
def home():

    return {
        "message": "AI Smart Finance Advisor Backend Running"
    }