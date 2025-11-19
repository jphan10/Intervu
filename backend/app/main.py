# FastAPI implementation
from fastapi import FastAPI

# Instantiate api isntance
app = FastAPI()

# Health check endpoint
@app.get("/health")
async def root():
    return {"message": "API is reachable!"}

# Define USER model using BaseModel
