import flet as ft

from ui.Common import MyButton, MyTitle


class Instruction(ft.UserControl):
    def __init__(self, next_state):
        self.next_state = next_state
        super().__init__()

    def build(self):
        return ft.Column(
            [MyTitle("Instruction"),
             ft.Container(
                 ft.Column([ft.Text("1. Insert list of products that you wanna buy.", size=20),
                            ft.Text("2. Wait for the system to download the offers from the internet.", size=20),
                            ft.Text("3. Select the offers that you wanna use.", size=20),
                            ft.Text("4. Press the button to open the offers in your browser.", size=20)])),
             ft.Container(height=200),
             MyButton("Go back!", lambda: self.next_state("main_menu"))], alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            height=760)
