import flet as ft

from details import Details
from productDetails import ProductDetails


class ProductPicker(ft.UserControl):
    def __init__(self, products: list[list[Details]]):
        super().__init__()
        print(products)
        self.products = products

    def build(self):
        build = [ft.Row(

            [ft.GridView(
                [ProductDetails(product) for product in list],
                expand=1,
                runs_count=5,
                max_extent=150,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
                auto_scroll=True,

            )], alignment=ft.MainAxisAlignment.CENTER
        ) for list in self.products]
        return build

        # for product in self.products:
        #     self.page.add(ft.SafeArea(ft.Text(product)))
