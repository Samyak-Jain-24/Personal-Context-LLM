import requests

def download_book():
    print("Initiating dataset download...")
    # URL for 'The Art of War' by Sun Tzu (Project Gutenberg Plain Text)
    url = "https://www.gutenberg.org/cache/epub/132/pg132.txt"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # Save the raw text to a file
        with open("art_of_war.txt", "w", encoding="utf-8") as file:
            # Slice the text to remove the massive Gutenberg legal boilerplate
            raw_text = response.text
            start_index = raw_text.find("I. LAYING PLANS")
            end_index = raw_text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
            
            clean_text = raw_text[start_index:end_index]
            file.write(clean_text)
            
        print("Success! 'art_of_war.txt' has been saved to your directory.")
        print(f"Dataset Size: {len(clean_text)} characters.")
    else:
        print("Failed to download dataset. Check your internet connection.")

if __name__ == "__main__":
    download_book() 