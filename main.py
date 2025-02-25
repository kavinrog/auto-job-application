# Authors: Kavinder Roghit Kanthen
#
# Date Started: February 24th, 2025
# Date Last Modified: February 25th, 2025
#
# Description:
# This script automates the process of filling out a job application form on a sample job portal using Selenium.
# It reads user details from a JSON file, navigates to the application page, and auto-fills various form fields,
# including text fields, radio buttons, and dropdown menus. Additionally, it detects CAPTCHA challenges and pauses
# execution to allow manual completion before proceeding with form submission. This automation helps save time
# and reduces human errors in repetitive job application processes.

import json
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_user_details(filepath):
    """Load user details from a JSON file."""
    with open(filepath, "r") as file:
        return json.load(file)

def detect_captcha(driver):
    """Detect if CAPTCHA is present."""
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "captcha")))
        logging.warning("CAPTCHA detected. Waiting for manual input.")
        return True
    except TimeoutException:
        return False

def fill_application_form(driver, user_details):
    """Navigates to the sample job application page and fills the form using provided details."""
    sample_url = "http://localhost:8000/application.html"  
    driver.get(sample_url)

    logging.info("Opened job application page.")

    # Wait until form is loaded
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "name")))

    # Fill the form fields
    driver.find_element(By.ID, "name").send_keys(user_details["name"])
    driver.find_element(By.ID, "email").send_keys(user_details["email"])
    driver.find_element(By.ID, "experience").send_keys(user_details["experience"])

    # Handle gender selection
    gender = user_details.get("gender", "").lower()
    if gender == "male":
        driver.find_element(By.ID, "gender_male").click()
    elif gender == "female":
        driver.find_element(By.ID, "gender_female").click()

    # Handle dropdown selection
    position_dropdown = Select(driver.find_element(By.ID, "job_position"))
    position_dropdown.select_by_visible_text(user_details["position"])

    logging.info("Filled application form successfully.")

    # CAPTCHA handling
    if detect_captcha(driver):
        while detect_captcha(driver):
            time.sleep(5)
        logging.info("CAPTCHA completed manually.")

    # Submit the form
    driver.find_element(By.ID, "submit").click()
    logging.info("Form submitted successfully.")

def main():
    """Main function to load user details and initiate Selenium automation."""
    user_details = load_user_details("user_data.json")
    
    # Initialize WebDriver with options
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)  # Ensure ChromeDriver is installed

    try:
        fill_application_form(driver, user_details)
        time.sleep(5)  # Allow time to review submission
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
