from fastapi import FastAPI

# Initialize the app
app = FastAPI(title="KAGE API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to KAGE API - Anime Scene Generator"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": "stable-diffusion-xl"}