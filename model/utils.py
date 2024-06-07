from abc import ABC, abstractmethod
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from model.details import Details
from enum import Enum


class sortedBy(Enum):
    # RELEVANT = "relevance"
    PRICE_ASC = "price"
    # PRICE_DESC = "price_desc"
    POPULARITY = "popularity"
    REVIEWS = "reviews"


class ScrapperStrategy(ABC):
    @abstractmethod
    def scrape_list_of_products(self, product_name: str, number_of_items) -> list[Details]:
        pass


def create_driver():
    ua = UserAgent()
    user_agent = ua.random
    chrome_options = Options()
    chrome_options.add_argument(f'--user-agent={user_agent}')
    # chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)

    # driver.minimize_window()
    return driver


