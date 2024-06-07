import flet as ft

from ui.Common import MyTitle


class Summary(ft.UserControl):
    def __init__(self, go_next, products):
        super().__init__()
        self.go_next = go_next
        self.products = products

    def build(self):
        return ft.Column([MyTitle("Summary"),
                          ft.Column([ft.Text(product.name, text_align=ft.TextAlign.CENTER, size=15) for product in
                                     self.products])],
                         alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                         height=760)
