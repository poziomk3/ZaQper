import time

from model import Details
from model.abstractScrapper import AbstractScrapper
from model.utils import  sortedBy


class GimmickScrapper(AbstractScrapper):

    def scrape_list_of_products(self, product_name: str, number_of_items: int) -> list[Details]:
        time.sleep(1)
        return [
                   Details("Organic Almond Butter", "12.99", "https://picsum.photos/200/300",
                           "https://picsum.photos/200/300"),
                   Details("Quinoa Grain", "8.49", "https://picsum.photos/200/300", "https://picsum.photos/200/300"),
                   Details("Dark Chocolate Bar", "3.75", "https://picsum.photos/200/300",
                           "https://picsum.photos/200/300"),
                   Details("Organic Honey", "6.25", "https://picsum.photos/200/300", "https://picsum.photos/200/300"),
                   Details("Chia Seeds", "5.99", "https://picsum.photos/200/300", "https://picsum.photos/200/300"),
                   Details("Coconut Oil", "10.50", "https://picsum.photos/200/300", "https://picsum.photos/200/300"),
                   Details("Kale Chips", "4.75", "https://picsum.photos/200/300", "https://picsum.photos/200/300"),
                   Details("Organic Green Tea", "7.99", "https://picsum.photos/200/300",
                           "https://picsum.photos/200/300"),
                   Details("Natural Peanut Butter", "5.49", "https://picsum.photos/200/300",
                           "https://picsum.photos/200/300"),
                   Details("Whole Grain Bread", "4.25", "https://picsum.photos/200/300",
                           "https://picsum.photos/200/300")
               ][:number_of_items]
