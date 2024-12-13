from terminal.processor import Processor

class ProductProcessor(Processor):
    
    def lookup_products_by_query(self, query):
        """
        Retrieves product ids according to threshold.
        """
        query_embedding = self.generate_embedding(query)
        threshold = 0.5 
        self.cursor.execute("""
            SELECT product_id, (1 - (embedding <=> %s::vector)) AS similarity
            FROM product_embeddings 
            WHERE (1 - (embedding <=> %s::vector)) > %s
            ORDER BY embedding <=> %s::vector LIMIT 5;
        """, (query_embedding, query_embedding, threshold, query_embedding))
        results = self.cursor.fetchall()
        return [result[0] for result in results]
    
    def lookup_similar_products(self, product_id: str):
        """
        Retrieve similar products given a product id
        """
        threshold = 0.5
        self.cursor.execute("""
            SELECT * FROM product_embeddings WHERE product_id = %s
        """, (product_id))
        prod_embedding = self.cursor.fetchall()
        self.cursor.execute("""
            SELECT product_id, (1 - (embedding <=> %s::vector)) AS similarity
            FROM product_embeddings 
            WHERE (1 - (embedding <=> %s::vector)) > %s
            ORDER BY embedding <=> %s::vector LIMIT 5;
        """, (prod_embedding, prod_embedding, threshold, prod_embedding))
        return self.cursor.fetchall()
    
    def find_related(self, query: str):
        related_product_ids = self.lookup_products_by_query(query)
        if related_product_ids:
            placeholder= ', '.join(['%s'] * len(related_product_ids))
            sql_query = f"SELECT * FROM products WHERE id IN ({placeholder})"
            self.cursor.execute(sql_query, related_product_ids)
            products = self.cursor.fetchall()
            products_in_order = []
            for id in related_product_ids:
                product = [dict(product) for product in products if product['id'] == id][0]
                products_in_order.append(product)
            return products_in_order
        return []