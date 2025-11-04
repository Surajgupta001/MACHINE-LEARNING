'''
Real-World Example: Multi-threading for I/O-Bound Tasks
Scenario: Web Scraping
Web scraping often involves making multiple network requests to fetch web pages. These tasks are I/O-bound because they spend most of their time waiting for responses from web servers. Using multi-threading can significantly speed up the scraping process by allowing multiple requests to be made concurrently.
'''

import threading
import requests
import time
from bs4 import BeautifulSoup

urls = [
    'https://www.python.org',
    'https://www.wikipedia.org',
    'https://www.github.com',
    'https://www.stackoverflow.com'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Finished fetching all URLs.")