from model.scrapperList import scrappers


def get_scrapper_names():
    return list(scrappers.keys())


def get_scrapper_strategy(name, sorted_by):
    return scrappers[name](sorted_by)
