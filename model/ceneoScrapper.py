from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from model import Details
from model.scrapper import create_driver, ScrapperStrategy, sortedBy


class CeneoScrapper(ScrapperStrategy):
    def __init__(self, sorted_by: sortedBy | None = None):
        self.url = f"https://www.ceneo.pl/;szukaj-"
        self.sorted_by = sorted_by

    def scrape_list_of_products(self, product_name: str, number_of_items: int) -> list[Details]:
        driver = create_driver()
        driver.get(self.url + product_name + self.get_url_suffix())
        result = [self.strip_details(element.get_attribute("innerHTML")) for element in
                  driver.find_elements(By.CLASS_NAME, "cat-prod-row")[:number_of_items]]

        if len(result) == 0:
            print(driver.page_source)
        return result

    def get_url_suffix(self) -> str:
        if self.sorted_by == sortedBy.PRICE_ASC.value:
            return ";0112-0.htm"
        elif self.sorted_by == sortedBy.POPULARITY.value:
            return ";0115-1.htm"
        else:
            return ""

    def strip_details(self, html: str) -> Details:
        soup = BeautifulSoup(html, "html.parser")
        product_name = soup.find('strong', class_='cat-prod-row__name').text.strip()

        details_link = 'https://www.ceneo.pl' + soup.find('a').get('href')

        image_tag = soup.find('div', class_='cat-prod-row__foto').find('img')

        if image_tag['src'].startswith('//'):
            image_link = 'https:' + image_tag['src']
        else:
            image_link = 'https:' + image_tag['data-original']

        price_tag = soup.find('div', class_='cat-prod-row__price').find('span', class_='price')
        price = price_tag.text.strip()

        return Details(product_name, price, image_link, details_link)
