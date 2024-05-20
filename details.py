from bs4 import BeautifulSoup


class Details:
    def __init__(self, name=None, price=None, image_link=None, details_link=None):
        self.name = name
        self.price = price
        self.image_link = image_link
        self.details_link = details_link

    def __str__(self):
        return f"{self.name}: {self.price} ({self.details_link}) - {self.image_link}"

    def __repr__(self):
        return f"{self.name}: {self.price} ({self.details_link}) - {self.image_link}"


def strip_details(html: str) -> Details:
    soup = BeautifulSoup(html, "html.parser")
    product_name = soup.find('strong', class_='cat-prod-row__name').text.strip()

    details_link = soup.find('a').get('href')
    details_link = 'https://www.ceneo.pl' + details_link
    # Extract image link
    image_tag = soup.find('div', class_='cat-prod-row__foto').find('img')
    if image_tag['src'].startswith('//'):
        image_link = 'https:' + image_tag['src']
    else:
        image_link = 'https:'+image_tag['data-original']

    # Extract price
    price_tag = soup.find('div', class_='cat-prod-row__price').find('span', class_='price')
    price = price_tag.text.strip()

    # Print the extracted information
    return Details(product_name, price, image_link, details_link)
