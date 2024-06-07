from abc import ABC, abstractmethod

from model import Details
from model.utils import sortedBy


class AbstractScrapper(ABC):
    """
    Abstract class for scrapper
    """

    def __init__(self, sorted_by: sortedBy | None = None):
        self.sorted_by = sorted_by

    @abstractmethod
    def scrape_list_of_products(self, product_name: str, number_of_items: int) -> list[Details]:
        """
        Scrape list of products
        :param product_name: name of product
        :param number_of_items: number of items to scrape
        :return: list of Details
        """
        pass
