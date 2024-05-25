import flet as ft


class MyButton(ft.UserControl):
    def __init__(self, text, on_click):
        super().__init__()
        self.text = text
        self.on_click = on_click

    def build(self):
        return ft.Row([
            ft.ElevatedButton(
                content=ft.Container(content=ft.Text(self.text, text_align=ft.TextAlign.CENTER, size=15),
                                     padding=10),
                on_click=lambda _: self.on_click(), bgcolor="blue",
                animate_size=True,
                color="white", width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)


class MyTitle(ft.UserControl):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def build(self):
        return ft.Text(self.text, text_align=ft.TextAlign.CENTER, size=34, font_family="Arial", italic=True)

# class ColWrapper(ft.UserControl):
#         def __init__(self, content, ref=None):
#             super().__init__()
#             self.content = content
#             self.ref = ref
#
#         def build(self):
#             return ft.Column(
#                 self.content,
#                 ref=self.ref,
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
#                 height=760)
