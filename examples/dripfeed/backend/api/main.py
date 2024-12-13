from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .processor import ProductProcessor 
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
processor = ProductProcessor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RelatedPayload(BaseModel):
    query: str

class SimilarPayload(BaseModel):
    product_id: str

@app.post("/api/related")
async def related(payload: RelatedPayload):
    query = payload.query
    if not query:
        return {"error": "Missing 'query' is required."}, 400
    products = processor.find_related(query)
    return { "data": products }

@app.post("/api/similar")
async def similar(payload: SimilarPayload):
    id = payload.product_id
    if not id:
        return {"error": "Missing 'product_id' is required."}, 400
    products = processor.lookup_similar_products(id)
    return { "data": products }