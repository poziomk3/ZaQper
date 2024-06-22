import unittest

from scrapper.ceneoScrapper import CeneoScrapper
from scrapper.gimmickScrapper import GimmickScrapper
from scrapper.olxScrapper import OlxScrapper


class TestScrapper(unittest.TestCase):
    def setUp(self):
        self.OLX= OlxScrapper()
        self.CENEO = CeneoScrapper()
        self.gimmick = GimmickScrapper()

    def read_html_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()


    def test_olx_scrapper(self):
        html = self.read_html_file('data/olx.html')
        details = self.OLX.strip_details(html)
        print(details)
        self.assertEqual(details.name, 'Sok jagoda kamczacka jabłko')
        self.assertEqual(details.price, '20')
        self.assertEqual(details.details_link, 'https://www.olx.pl/d/oferta/sok-jagoda-kamczacka-jablko-CID757-ID10DbfR.html')
        self.assertEqual(details.image_link,
                         'https://ireland.apollo.olxcdn.com:443/v1/files/hx7f901dqu0q3-PL/image;s=200x0;q=50')


    def test_ceneo_scrapper(self):
        html = self.read_html_file('data/ceneo.html')
        details = self.CENEO.strip_details(html)
        print(details)
        self.assertEqual(details.name, 'Dinozaury do kolorowania - z kredkami dookoła świata Olesiejuk')
        self.assertEqual(details.price, '10,10')
        self.assertEqual(details.details_link, 'https://www.ceneo.pl/152028439')
        self.assertEqual(details.image_link,
                         'https://image.ceneostatic.pl/data/products/152028439/f-dinozaury-do-kolorowania-z-kredkami-dookola-swiata-olesiejuk.jpg')