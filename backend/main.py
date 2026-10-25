from fastapi import FastAPI

app = FastAPI(title="Form Filler API")

@app.get("/")
def home():
    return {
    "message": "Form Filler backend is running!"
    }