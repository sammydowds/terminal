from terminal.ingestor import Ingestor 

class ProductIngestor(Ingestor):
    def save_embedding(self):
        return 
    def ingest(self):
        # look up products
        self.cursor.execute("SELECT * FROM products")
        for row in self.cursor:
            print(row)
        # loop through products (one by one)
        return True
