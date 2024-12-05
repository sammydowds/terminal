from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from .processor import ResumeProcessor
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()
processor = ResumeProcessor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str

class Payload(BaseModel):
    messages: List[Message] = Field(..., description="List of messages")

@app.post("/api/chat")
async def chat(payload: Payload):
    print(payload)
    messages = payload.messages
    query = messages[-1].content

    if not query:
        return {"error": "Missing 'query' is required."}, 400

    content = processor.retrieve_content(query)
    return StreamingResponse(processor.stream_completion(content, query), media_type="text/event-stream")