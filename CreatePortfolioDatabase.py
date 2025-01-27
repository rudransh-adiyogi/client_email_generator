import pandas as pd
import uuid
import chromadb ### create database for sementic search and retrieval

class Portfolio:
    def __init__(self,file_path="app/resource/my_portfolio.csv"):
        self.portfolio_df = pd.read_csv(file_path) ### portfolio of my company
        self.client = chromadb.PersistentClient('vectorstore') ### store in disk
        self.collection = self.client.get_or_create_collection(name="portfolio")
    def CreateDatabase(self):
        if not self.collection.count():
            for _, row in self.portfolio_df.iterrows():
                self.collection.add(documents=row["Techstack"],
                            metadatas={"links": row["Links"]},
                            ids=[str(uuid.uuid4())])
    def get_links(self,json_res):
        links = self.collection.query(query_texts=json_res['skills'], n_results=2).get('metadatas', [])
        return links