import time

from model import Details
from model.utils import  ScrapperStrategy,sortedBy


class GimmickScrapper(ScrapperStrategy):
    def __init__(self, sorted_by: sortedBy | None = None):
        self.sorted_by = sorted_by

    def scrape_list_of_products(self, product_name: str, number_of_items: int) -> list[Details]:
        time.sleep(1)
        return [
                   Details("Organic Almond Butter", "12.99", "https://picsum.photos/200/300",
                           "https://example.com/almond-butter"),
                   Details("Quinoa Grain", "8.49", "https://picsum.photos/200/300", "https://example.com/quinoa"),
                   Details("Dark Chocolate Bar", "3.75", "https://picsum.photos/200/300",
                           "https://example.com/dark-chocolate"),
                   Details("Organic Honey", "6.25", "https://picsum.photos/200/300", "https://example.com/honey"),
                   Details("Chia Seeds", "5.99", "https://picsum.photos/200/300", "https://example.com/chia-seeds"),
                   Details("Coconut Oil", "10.50", "https://picsum.photos/200/300", "https://example.com/coconut-oil"),
                   Details("Kale Chips", "4.75", "https://picsum.photos/200/300", "https://example.com/kale-chips"),
                   Details("Organic Green Tea", "7.99", "https://picsum.photos/200/300",
                           "https://example.com/green-tea"),
                   Details("Natural Peanut Butter", "5.49", "https://picsum.photos/200/300",
                           "https://example.com/peanut-butter"),
                   Details("Whole Grain Bread", "4.25", "https://picsum.photos/200/300",
                           "https://example.com/whole-grain-bread")
               ][:number_of_items]
