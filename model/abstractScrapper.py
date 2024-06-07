from abc import ABC, abstractmethod

from model import Details
from model.utils import sortedBy


class AbstractScrapper(ABC):
    @abstractmethod
    def __init__(self, sorted_by: sortedBy | None):
        pass

    @abstractmethod
    def scrape_list_of_products(self, product_name: str, number_of_items) -> list[Details]:
        pass
