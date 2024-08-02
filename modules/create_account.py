from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def create_account(email, password, captcha_solution):
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')
    driver.get("https://wtnmarket.net/register")

    time.sleep(3)

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    captcha_field = driver.find_element(By.NAME, "captcha")

    email_field.send_keys(email)
    password_field.send_keys(password)
    captcha_field.send_keys(captcha_solution)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(5)  # Wait for account creation process to complete
    driver.quit()
