import unittest

from model import AbstractScrapper
from model.endpoints import get_scrapper_names, get_scrapper_strategy
from scrapper.scrapperList import ScrapperName


class TestScrapper(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_scrappers_list(self):
        scrappers = get_scrapper_names()
        self.assertIsInstance(scrappers, list)

    def test_is_scrapper_available(self):
        self.assertIsInstance(get_scrapper_strategy(ScrapperName.OLX, "anything"), AbstractScrapper)
