import flet as ft

from ui.Common import MyTitle


class Summary(ft.UserControl):
    def __init__(self, go_next, products):
        super().__init__()
        self.go_next = go_next
        self.products = products

    def build(self):
        return ft.Column(
            [
                ft.Column(
                    [ft.Text("Summary", size=34),*[ft.Text(product.price + "  PLN ---- " + product.name, text_align=ft.TextAlign.CENTER, size=15) for
                     product in
                     self.products]])
            ],
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, height=760,
            width=1200)
