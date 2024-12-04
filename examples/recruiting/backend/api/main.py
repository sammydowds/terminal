from fastapi import FastAPI
from .processor import ResumeProcessor

app = FastAPI()
processor = ResumeProcessor()

@app.get("/api/chat")
async def root(query: str = ""):
    response = processor.process_query(query)
    return {"message": response }