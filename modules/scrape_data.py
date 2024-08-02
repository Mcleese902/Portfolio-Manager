from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def login_and_scrape(email, password):
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')
    driver.get("https://wtnmarket.net/login")

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    email_field.send_keys(email)
    password_field.send_keys(password)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(5)  # Wait for login to complete

    # Navigate to products page
    driver.get("https://wtnmarket.net/products")
    time.sleep(3)

    products = []

    while True:
        product_elements = driver.find_elements(By.CLASS_NAME, "product-list-item")

        for product in product_elements:
            title = product.find_element(By.CLASS_NAME, "product-title").text
            price = product.find_element(By.CLASS_NAME, "product-price").text
            vendor = product.find_element(By.CLASS_NAME, "product-vendor").text
            products.append({"title": title, "price": price, "vendor": vendor})

        next_button = driver.find_element(By.CLASS_NAME, "next-page")
        if next_button:
            next_button.click()
            time.sleep(3)
        else:
            break

    driver.quit()

    df = pd.DataFrame(products)
    df.to_csv("products.csv", index=False)

# Example usage
if __name__ == "__main__":
    login_and_scrape("your_email@example.com", "your_password")
