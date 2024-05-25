import time

import flet as ft

from details import Details
from scrapperStrategies import ceneoScrapper, sortedBy
from ui.Common import MyButton, MyTitle


class Instruction(ft.UserControl):
    def __init__(self, next_state):
        self.next_state = next_state
        super().__init__()

    def build(self):
        return ft.Column(
            [MyTitle("Instruction"),
             MyButton("Go back!", lambda: self.next_state("main_menu"))], alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            height=760)
