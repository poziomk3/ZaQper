import flet as ft

from details import Details


class ProductDetails(ft.UserControl):
    def __init__(self, product: Details):
        super().__init__()
        self.product = product

    def build(self):
        return ft.Container(
            bgcolor="red",
            aspect_ratio=1.0,
            content=ft.Image(src=self.product.image_link, aspect_ratio=1.0),
        )
