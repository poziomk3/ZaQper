from scrapper.ceneoScrapper import CeneoScrapper
from scrapper.gimmickScrapper import GimmickScrapper
from scrapper.olxScrapper import OlxScrapper

scrappers = {
    'Gimmick': GimmickScrapper,
    'Ceneo': CeneoScrapper,
    'OLX': OlxScrapper
}