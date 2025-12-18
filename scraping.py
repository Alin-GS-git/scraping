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
