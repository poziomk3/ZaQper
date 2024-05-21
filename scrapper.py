import threading
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import details


def create_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)
    # driver.minimize_window()
    return driver


# Function to fetch product details for a given product name
def fetch_product_details(product_name: str, driver: webdriver.Chrome) -> List[details.Details]:
    url = f"https://www.ceneo.pl/;szukaj-{product_name}"
    driver.get(url)
    elements: List[webdriver.remote.webelement.WebElement] = driver.find_elements(By.CLASS_NAME, "cat-prod-row")[:9]
    # for element in elements:
    #     print(product_name)

    return [details.strip_details(element.get_attribute("innerHTML")) for element in elements]


def fetch_list_of_items(products: List[str]) -> List[List[details.Details]]:
    driver = create_driver()
    result = []


    for product in products:
        result.append(fetch_product_details(product, driver))
        # time.sleep(1)
    driver.quit()
    print(*result,sep='\n')
    return result


fetch_list_of_items(["nozyczki", "kosiarka", "błyszczyk","kartofle","ziemniak"] )
