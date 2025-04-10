from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver using webdriver-manager
service = Service(ChromeDriverManager().install())

# Base URL of the form
base_url = "https://efg770.github.io"

# Data to fill in the form
form_data = {
    "delek1": "025566998",
    "delek2": "0585551234"
}

# Start a new browser session
driver = webdriver.Chrome(service=service)

try:
    # Open the form URL
    driver.get(base_url)

    # Fill in the form fields
    delek1_input = driver.find_element(By.ID, "delek1")
    delek1_input.send_keys(form_data["delek1"])

    delek2_input = driver.find_element(By.ID, "delek2")
    delek2_input.send_keys(form_data["delek2"])

    # Keep the browser open for manual interaction
    print("Form fields filled. You can now manually submit the form if needed.")

finally:
    # Close the browser when you're done
    input("Press Enter to close the browser...")
    driver.quit()