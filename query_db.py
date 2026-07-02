from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def run_semantic_search():
    # 1. Initialize the exact same embedding model so the math matches
    print("Loading local embedding model...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Point to our existing database directory on disk
    persist_directory = "chroma_db"
    print(f"Connecting to the local database at '{persist_directory}'...")
    
    db = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embedding_model
    )
    
    # 3. Define a conceptual question
    # Notice that the phrase "look after your troops" does not appear exactly like this in the book.
    query = "How should a commander look after their troops?"
    print(f"\n🔍 Querying database for meaning: '{query}'")
    
    # 4. Retrieve the top 2 closest matching text chunks
    # k=2 tells the database to return only the top two most relevant snippets
    docs = db.similarity_search(query, k=2)
    
    # 5. Display what the database retrieved
    print(f"\n🎯 Found {len(docs)} highly relevant context chunks:\n")
    
    for index, doc in enumerate(docs, start=1):
        print(f"--- RETRIEVED CHUNK #{index} ---")
        print(doc.page_content.strip())
        print("-" * 32 + "\n")

if __name__ == "__main__":
    run_semantic_search()