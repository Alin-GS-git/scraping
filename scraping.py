# from bs4 import beautifulsoup4
# import requests

# url="https://khwopa.edu.np/"
# response = requests.get(url)

# soup = beautifulsoup4(response.text, "html.parser")

# title = soup.title.text
# headings = [h.text.strip() for h in soup.find_all("h1")]

# print("Page Title:", title)
# print("Headings:")

# for h in headings:
#     print("-", h)

# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title.text)
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: URL
url = "http://books.toscrape.com/"

# Step 2: Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract book titles and prices
titles = []
prices = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    
    titles.append(title)
    prices.append(price)

# Step 4: Save to DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

print(df)

# Step 5: Save to CSV
df.to_csv("books.csv", index=False)
print("\nData saved to books.csv")
