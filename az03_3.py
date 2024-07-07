import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# URL of the website to scrape
url = 'https://www.divan.ru/category/divany'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant elements containing the prices
# Note: Update the selectors based on the actual structure of the website
prices = []
for price_tag in soup.select('div.price'):
    price_text = price_tag.get_text(strip=True)
    # Remove non-numeric characters and convert to float
    price = float(''.join(filter(str.isdigit, price_text)))
    prices.append(price)

# Convert the prices to a DataFrame
df_prices = pd.DataFrame(prices, columns=['Price'])

# Save to CSV file
df_prices.to_csv('sofa_prices.csv', index=False)

# Calculate the average price
average_price = df_prices['Price'].mean()
print(f'Average price of sofas: {average_price:.2f}')

# Create a histogram of prices
plt.hist(df_prices['Price'], bins=30, edgecolor='black')
plt.title('Histogram of Sofa Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

