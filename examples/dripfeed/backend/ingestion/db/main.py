from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pgvector.sqlalchemy import Vector

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'  
    id: Mapped[str] = mapped_column(String, primary_key=True) 
    name: Mapped[str] = mapped_column(String)  
    department: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    ul: Mapped[str] = mapped_column(String) 
    images: Mapped[List[str]] = mapped_column(String) 
    sizes: Mapped[dict] = mapped_column(String)  
    long_description: Mapped[str] = mapped_column(String)  
    color: Mapped[str] = mapped_column(String)  
    seasons: Mapped[str] = mapped_column(String)  
    brand_code: Mapped[str] = mapped_column(String)  
    brand_name: Mapped[str] = mapped_column(String)  
    brand_logo: Mapped[str] = mapped_column(String)  
    color_options: Mapped[List[str]] = mapped_column(String)  
    gender: Mapped[str] = mapped_column(String)
    prices: Mapped[dict] = mapped_column(String)

class ProductEmbeddings(Base):
    __tablename__ = 'product_embeddings'
    productId: Mapped[str] = mapped_column(String, primary_key=True) 
    embedding: Mapped[Vector] = mapped_column(Vector(1536)) 

def init():
    engine = create_engine(echo=True)