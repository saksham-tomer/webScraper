import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_article_content(url):
    try:
        #GET request to the URL
        response = requests.get(url)
        # Checking if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extracting article heading and body
            heading = soup.find('h1').get_text().strip()
            body = soup.find('article').get_text().strip()
            return heading, body
        else:
            return None, None
    except Exception as e:
        print(f"Error occurred while processing {url}: {e}")
        return None, None

def main():
    try:
        df = pd.read_excel("your_file.xlsx")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    
    if 'URL_ID' not in df.columns or 'URL' not in df.columns:
        print("Error: Missing required columns in the Excel file.")
        return
    
    # Create or open the output text file
    with open("URL_ID.txt", "w", encoding="utf-8") as f:
        # Iterating over each row in the DataFrame
        for index, row in df.iterrows():
            url_id = row['URL_ID']
            url = row['URL']

            heading, body = extract_article_content(url)
            if heading and body:
                # Writing the data to the text file
                f.write(f"URL ID: {url_id}\n")
                f.write(f"Article Heading: {heading}\n")
                f.write(f"Article Body: {body}\n\n")
                print(f"Processed URL ID: {url_id}")
            else:
                print(f"Failed to process URL ID: {url_id}")

if __name__ == "__main__":
    main()
