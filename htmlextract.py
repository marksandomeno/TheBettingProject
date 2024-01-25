from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all text from the parsed HTML
text = soup.get_text(separator='\n', strip=True)

# Save the extracted text to a file
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("Text content saved to 'extracted_text.txt'")
