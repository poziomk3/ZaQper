import flet as ft

from details import Details


class ProductPicker(ft.UserControl):
    def __init__(self, products: list[list[Details]]):
        super().__init__()
        print(products)
        self.products = products
        print(products)

    def build(self):
        build = ft.Column([ft.Row(

            [ft.Text("item"), ft.GridView(
                [ProductDetails(product) for product in prod_list],
                expand=1,
                runs_count=5,
                max_extent=150,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
                auto_scroll=True,

            )], alignment=ft.MainAxisAlignment.CENTER
        ) for prod_list in self.products])
        return build

        # for product in self.products:
        #     self.page.add(ft.SafeArea(ft.Text(product)))


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


class ListCreator(ft.UserControl):
    def __init__(self, products: list[list[Details]]):
        super().__init__()
        self.products = products

    def build(self):
        return ft.Column([ft.Text("list-creator")
                          ])
