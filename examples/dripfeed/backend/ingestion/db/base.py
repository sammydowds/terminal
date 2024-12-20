from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String, JSON
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import ARRAY


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'  
    id: Mapped[str] = mapped_column(String, primary_key=True) 
    name: Mapped[str] = mapped_column(String)  
    department: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    ul: Mapped[str] = mapped_column(String) 
    image: Mapped[str] = mapped_column(String) 
    sizes: Mapped[dict] = mapped_column(JSON)  
    long_description: Mapped[str] = mapped_column(String)  
    color: Mapped[str] = mapped_column(String)  
    seasons: Mapped[str] = mapped_column(String)  
    brand_code: Mapped[str] = mapped_column(String)  
    brand_name: Mapped[str] = mapped_column(String)  
    brand_logo: Mapped[str] = mapped_column(String)  
    target_url: Mapped[str] = mapped_column(String)  
    color_options: Mapped[List[str]] = mapped_column(String)  
    gender: Mapped[str] = mapped_column(String)
    prices: Mapped[dict] = mapped_column(JSON)

class ProductEmbeddings(Base):
    __tablename__ = 'product_embeddings'
    product_id: Mapped[str] = mapped_column(String, primary_key=True) 
    embedding: Mapped[Vector] = mapped_column(Vector(1536)) 