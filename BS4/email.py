import requests
from bs4 import BeautifulSoup
import re

url = "URL PATH"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

for email in emails:
    print(email)
