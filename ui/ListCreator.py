import flet as ft

from ui.Common import MyTitle, MyButton


class ListCreator(ft.UserControl):
    def __init__(self, next_state):
        self.products = []
        super().__init__()
        self.next_state = next_state
        self.list = ft.Column()
        self.textField: ft.Ref[ft.TextField] = ft.Ref[ft.TextField]()

    def build(self):
        return ft.Column(
            [MyTitle("Zaqper"),
             ft.TextField(label="Product you wanna buy!", on_submit=lambda _: self.add_product_to_list(),
                          ref=self.textField),
             MyButton("Add product", lambda: self.add_product_to_list()),
             MyButton("Next", lambda: self.next_state("product_picker")),
             ft.Container(ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                 ft.Column([self.list],
                           scroll=ft.ScrollMode.ADAPTIVE, width=400
                           )], height=400),
                          )],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, height=760,
        )

    def add_product_to_list(self):
        if self.textField.current.value == "":
            return
        self.products.append(self.textField.current.value)
        self.list.controls.append(ft.Text(self.textField.current.value, text_align=ft.TextAlign.CENTER, size=30))
        self.textField.current.value = ""
        self.textField.current.focus()
        self.update()
