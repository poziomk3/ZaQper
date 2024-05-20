import flet as ft

from productDetails import ProductDetails


class ProductPicker(ft.UserControl):
    def __init__(self, products: list[str]):
        super().__init__()
        print(products)
        self.products = products

    def build(self):
        return ft.Container(
            content=self.cut_to_3_rows()
        )

        # for product in self.products:
        #     self.page.add(ft.SafeArea(ft.Text(product)))

    def cut_to_3_rows(self):
        if len(self.products) % 3 != 0:
            return None

        rows = len(self.products) // 3

        return ft.Column([ft.Row([ProductDetails(self.products[:rows])]),
                          ft.Row([ProductDetails(self.products[rows: 2 * rows])]),
                          ft.Row([ProductDetails(self.products[2 * rows:])])])
