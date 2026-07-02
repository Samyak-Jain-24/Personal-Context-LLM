import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def build_vector_database():
    # 1. Locate and Load the document
    file_path = "art_of_war.txt"
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}. Run fetch_data.py first!")
        return
        
    print("Loading text document...")
    loader = TextLoader(file_path, encoding="utf-8")
    raw_document = loader.load()

    # 2. Chunk the text (Our strategy from Step 2)
    print("Slicing text into strategic chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(raw_document)
    print(f"Generated {len(chunks)} chunks.")

    # 3. Initialize the local Embedding Model
    # This downloads a ~90MB model file the first time you run it, then executes locally.
    print("\nInitializing local HuggingFace Embedding Model ('all-MiniLM-L6-v2')...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Create and Populate the Vector Database
    # We specify a directory where Chroma will save its mathematical indices onto your hard drive
    persist_directory = "chroma_db"
    print(f"Generating embeddings and baking them into local database folder '{persist_directory}'...")
    
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    
    print("\n🎉 SUCCESS! Database built and saved to disk.")
    print("ChromaDB is now holding your vectorized knowledge base.")

if __name__ == "__main__":
    build_vector_database()