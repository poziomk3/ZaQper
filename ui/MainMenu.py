import flet as ft

from ui.Common import MyButton, MyTitle


class MainMenu(ft.UserControl):
    def __init__(self, next_state):
        super().__init__()
        self.next_state = next_state

    def build(self):
        return ft.Column(
            [MyTitle("ZaQper"),
             MyButton("Start", lambda: self.next_state("list_creator")),
             MyButton("Learn how it works", lambda: self.next_state("instruction")),
             ],
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER,height=760)
