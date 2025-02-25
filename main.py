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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def load_user_details(filepath):
    """
    Load user details from a JSON file.
    Expected JSON format example:
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "experience": "5",
      "position": "Software Engineer",
      "gender": "female"
    }
    """
    with open(filepath, "r") as file:
        return json.load(file)

def detect_captcha(driver):
    """
    Check if a CAPTCHA is present on the page.
    Returns True if CAPTCHA is found.
    """
    try:
        driver.find_element(By.ID, "captcha")
        return True
    except NoSuchElementException:
        return False

def fill_application_form(driver, user_details):
    """
    Navigates to the sample job application page and fills the form using the provided user details.
    """
    sample_url = "http://localhost:8000/application.html"  # Ensure this is the correct URL for testing
    driver.get(sample_url)
    time.sleep(2)  # Wait for page to load

    # Fill out the form fields
    driver.find_element(By.ID, "name").send_keys(user_details["name"])
    driver.find_element(By.ID, "email").send_keys(user_details["email"])
    driver.find_element(By.ID, "experience").send_keys(user_details["experience"])

    # Handle radio buttons for gender selection
    gender = user_details.get("gender", "").lower()
    if gender == "male":
        driver.find_element(By.ID, "gender_male").click()
    elif gender == "female":
        driver.find_element(By.ID, "gender_female").click()

    # Handle dropdown selection for job position
    position_dropdown = Select(driver.find_element(By.ID, "job_position"))
    position_dropdown.select_by_visible_text(user_details["position"])

    # Detect and handle CAPTCHA challenges
    if detect_captcha(driver):
        print("CAPTCHA detected. Please solve it manually.")
        while detect_captcha(driver):
            time.sleep(5)
        print("CAPTCHA completed.")

    # Submit the form
    driver.find_element(By.ID, "submit").click()
    print("Form submitted successfully.")

def main():
    """
    Main function to load user details and initiate the Selenium automation.
    """
    user_details = load_user_details("user_data.json")  # Ensure the correct path to the JSON file
    driver = webdriver.Chrome()  # Make sure ChromeDriver is properly installed and set up

    try:
        fill_application_form(driver, user_details)
        time.sleep(5)  # Allow time to review the submission
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
