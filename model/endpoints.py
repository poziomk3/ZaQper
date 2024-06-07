from model import AbstractScrapper
from scrapper.scrapperList import scrappers


def get_scrapper_names() -> list[str]:
    return list(scrappers.keys())


def get_scrapper_strategy(name: str, sorted_by: str) -> AbstractScrapper:
    return scrappers[name](sorted_by)
