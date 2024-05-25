class Details:
    def __init__(self, name=None, price=None, image_link=None, details_link=None):
        self.name = name
        self.price = price
        self.image_link = image_link
        self.details_link = details_link

    def __str__(self) -> str:
        return f"{self.name}: {self.price} ({self.details_link}) - {self.image_link}"

    def __repr__(self) -> str:
        return f"{self.name}: {self.price} ({self.details_link}) - {self.image_link}"
