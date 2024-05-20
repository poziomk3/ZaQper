import flet as ft


class ProductDetails(ft.UserControl):
    def __init__(self, product):
        super().__init__()
        self.product = product

    def build(self):
        return ft.Container(
            content=ft.Text(self.product),
        )
