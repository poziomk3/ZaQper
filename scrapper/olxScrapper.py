from model import AbstractScrapper, Details


class OlxScrapper(AbstractScrapper):
    def scrape_list_of_products(self, product_name: str, number_of_items) -> list[Details]:
        return []
