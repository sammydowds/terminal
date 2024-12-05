from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from .processor import ResumeProcessor

app = FastAPI()
processor = ResumeProcessor()

@app.get("/api/chat")
async def root(q: str = "", stream: bool = False):
    content = processor.retrieve_content(q)
    if stream:
        return StreamingResponse(processor.stream_completion(content, q), media_type="text/event-stream")
    else:
        response = processor.completion(content, q)
        return { "message": response }