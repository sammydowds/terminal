from terminal.ingestor import Ingestor 
import psycopg2

class ProductIngestor(Ingestor):
    def save_embedding(self, productId: str, embedding: list[str]):
        try:
            self.cursor.execute("INSERT INTO product_embeddings (product_id, embedding) VALUES (%s, %s)", (productId, embedding))
            self.db.commit()
            return True
        except psycopg2.Error as e:
            self.db.rollback()
            raise Exception(f"Failed to save embedding: {e}")

    def ingest(self):
        try:
            # select attributes to use in embeddings
            self.cursor.execute("SELECT long_description, id FROM products")
            # note: only do below for local, small data sets 
            for row in self.cursor.fetchall():
                try:
                    context, product_id = row
                    print(f"Processing Product ID: {product_id}")
                    embedding = self.generate_embedding(context)
                    self.save_embedding(product_id, embedding)
                except Exception as e:
                    print(f"Error processing Product ID {product_id}: {e}")
            return True
        except Exception as e:
            print(f"Database query failed: {e}")
            return False

