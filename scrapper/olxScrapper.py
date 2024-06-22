from bs4 import BeautifulSoup

from model import AbstractScrapper, Details
from model.utils import create_driver
from selenium.webdriver.common.by import By


class OlxScrapper(AbstractScrapper):
    url = f"https://www.olx.pl/oferty/q-"

    def scrape_list_of_products(self, product_name: str, number_of_items) -> list[Details]:
        driver = create_driver()
        driver.get(self.url + product_name)
        results = driver.find_elements(By.CSS_SELECTOR, '[data-testid="l-card"]')

        return [self.strip_details(element.get_attribute("innerHTML")) for element in
                results[:number_of_items]]

    def strip_details(self, html: str) -> Details:
        soup = BeautifulSoup(html, "html.parser")
        product_name_tag = soup.find('h6')
        product_name = product_name_tag.text.strip() if product_name_tag else 'N/A'

        # Extract details link
        details_link_tag = soup.find('a', href=True)
        details_link = "https://www.olx.pl" + details_link_tag['href'] if details_link_tag else 'N/A'

        # Extract image link
        image_tag = soup.find('img', src=True)
        image_link = image_tag['src'] if image_tag else 'N/A'

        # Extract price
        price_tag = soup.find('p', {'data-testid': 'ad-price'})
        price = price_tag.text.strip() if price_tag else 'N/A'
        price = price.replace('zł', '').replace(' ', '').replace('\n', '').replace('\t', '')
        return Details(product_name, price, image_link, details_link)
