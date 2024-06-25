import enum

from scrapper.ceneoScrapper import CeneoScrapper
from scrapper.gimmickScrapper import GimmickScrapper
from scrapper.olxScrapper import OlxScrapper


class ScrapperName(enum.Enum):
    OLX = 'OLX'
    CENEO = 'Ceneo'
    GIMMICK = 'Gimmick'


scrappers = {
    'OLX': OlxScrapper,
    'Ceneo': CeneoScrapper,
    'Gimmick': GimmickScrapper,

}
