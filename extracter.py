from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Amazon India
driver.get("https://www.amazon.in")

# Maximize the browser window
driver.maximize_window()

# Search for 'lg soundbar'
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys("lg soundbar")
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for the page to load

# Fetch all product elements and prices
products = driver.find_elements(By.CSS_SELECTOR, '.s-main-slot .s-result-item')
product_price_dict = {}

for product in products:
    name = ""
    try:
        name = product.find_element(By.CSS_SELECTOR, 'h2 a span').text
        price_element = product.find_element(By.CSS_SELECTOR, '.a-price-whole')
        price = int(price_element.text.replace(",", ""))
    except:
        price = 0  # Handle missing price cases
    product_price_dict[name] = price

# Sort products by price
sorted_products = sorted(product_price_dict.items(), key=lambda item: item[1])

# Print sorted products
for name, price in sorted_products:
    print(f"{price} {name}")

# Close the browser
driver.quit()
