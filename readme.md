
# Zaqper

The application facilitates quick search and comparison of offers on various online platforms.

## The application workflow is as follows:
1. The user enters the list of  names of the products he is looking for.
2. The application searches for offers on various online platforms.
3. The application displays the offers found.
4. The user can adjust the search criteria.
5. The application displays the offers found again.
6. The user can click on offers and go to the offer page.


## Project structure

1. model - contains classes representing the structure of the application
2. view - contains classes responsible for the graphical interface of the application
3. controller - contains classes responsible for the logic of the application
4. scrapper - contains classes responsible for scrapping data from online platforms
5. run.py - main file of the application


## API


The application follows an easy pattern: _Scrapper_ is a directory containing all available scrappers (sources where offers come from). Each scrapper is a class that inherits from the abstract class _AbstractScrapper_ and implements the method _scrape_list_of_products_. The method _scrape_list_of_products_ should return a list of _Details_ objects. The _Details_ class is a class representing the structure of an offer. The _Details_ class should contain the following fields:
- name: str
- price: str
- image_link: str
- details_link: str

## How to add a new scrapper?

1. Create a new class in the scrapper directory that inherits from the _AbstractScrapper_ class.
2. Implement the _scrape_list_of_products_ method.
3. Add the scrapper to _scrappers_ in the _scrapperList.py_ and the name of the scrapper to the _ScrapperName_ class.

