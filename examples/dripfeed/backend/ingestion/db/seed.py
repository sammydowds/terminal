from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import json
from sqlalchemy.orm import sessionmaker
from base import Base, Product  # Import the Product model

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def init_db():
    Base.metadata.create_all(engine)

def seed_data():
    """
    Seeds sample products.
    """
    products = []
    with open('./sample_data/products.json') as f:
        products = json.load(f)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    for product in products:
        new_product = Product(
            id=product.get('id'),
            name=product.get('name'),
            department=product.get('department'),
            type=product.get('type'),
            ul=product.get('ul'),
            image=product.get('image'), 
            sizes=product.get('sizes', {}),
            long_description=product.get('long_description'),
            color=product.get('color'),
            seasons=product.get('seasons'),
            brand_code=product.get('brand_code'),
            brand_name=product.get('brand_name'),
            brand_logo=product.get('brand_logo'),
            target_url=product.get('target_url'),
            color_options=product.get('color_options', []),
            gender=product.get('gender'),
            prices=product.get('prices', {})
        )
        session.add(new_product)

    session.commit()
    session.close()

def create_vector_extension():
    """Create the vector extension in the database."""
    with engine.connect() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

if __name__ == "__main__":
    create_vector_extension()
    init_db()
    seed_data()
