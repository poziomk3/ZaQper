from model import AbstractScrapper
from scrapper.scrapperList import scrappers, ScrapperName


def get_scrapper_names() -> list[str]:
    return [name.value for name in ScrapperName]


def get_scrapper_strategy(name: ScrapperName, sorted_by: str) -> AbstractScrapper:
    return scrappers[name.value](sorted_by)
