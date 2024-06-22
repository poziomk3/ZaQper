from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from enum import Enum


class sortedBy(Enum):
    # RELEVANT = "relevance"
    POPULARITY = "popularity"
    PRICE_ASC = "price"
    # PRICE_DESC = "price_desc"
    REVIEWS = "reviews"


def create_driver() -> webdriver.Chrome:
    ua = UserAgent()
    user_agent = ua.random
    chrome_options = Options()
    chrome_options.add_argument(f'--user-agent={user_agent}')
    # chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)

    driver.minimize_window()
    return driver
