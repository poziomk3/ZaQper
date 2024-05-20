from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import details

# Configure Chrome options to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run the browser in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Start a new instance of Chrome WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()
# URL of the webpage you want to fetch HTML from
url = "https://www.ceneo.pl/;szukaj-"

# Navigate to the URL

product = ["szminka"]

for i in product:
    url = "https://www.ceneo.pl/;szukaj-" + i
    driver.get(url)
    driver.minimize_window()
    elements: List[WebElement] = driver.find_elements(By.CLASS_NAME, "cat-prod-row")
    print(elements[4].get_attribute("innerHTML"))

    for element in elements:
        print(details.strip_details(element.get_attribute("innerHTML")))

driver.quit()

# Now 'html' contains the HTML source of the webpage
file_path = "example.html"

# with open(file_path, "w") as file:
#     file.write(html)
