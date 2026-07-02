from langchain_text_splitters import RecursiveCharacterTextSplitter

def analyze_and_chunk_document():
    # 1. Read the substantial dataset we pulled in Step 1
    print("Reading 'art_of_war.txt'...")
    with open("art_of_war.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()
    
    print(f"Total characters in raw document: {len(raw_text)}")

    # 2. Configure the intelligent text splitter
    # We set a chunk size of 1000 characters with a 150-character overlap safety buffer
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    # 3. Chop the book up into structured LangChain Document objects
    print("\nExecuting recursive character splitting...")
    chunks = text_splitter.create_documents([raw_text])
    
    # 4. Print Pipeline Analytics
    print(f"Successfully generated {len(chunks)} independent text chunks!")
    
    # 5. Inspect a few chunks closely to understand what they look like
    print("\n" + "="*40)
    print("🔬 INSPECTING CHUNK #5")
    print("="*40)
    print(chunks[5].page_content)
    
    print("\n" + "="*40)
    print("🔬 INSPECTING CHUNK #6 (Notice the sliding overlap text at the start!)")
    print("="*40)
    print(chunks[6].page_content)

if __name__ == "__main__":
    analyze_and_chunk_document()