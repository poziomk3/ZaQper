import time
from typing import List

import flet as ft

from details import Details
from scrapperStrategies import ScrapperStrategy, create_driver
from state import MainMenuState, State, InstructionState
import webbrowser


class Controller:
    _state = None
    page = None

    def __init__(self):
        print("Controller created")

    def run(self, page: ft.Page):
        self.page = page
        self.page.window_width = 1400  # window's width is 200 px
        self.page.window_height = 800  # window's height is 200 px
        self.page.window_resizable = False
        self.transition_to(MainMenuState())
        self.page.update()

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")

        self._state = state
        self._state._context = self
        if not isinstance(state, MainMenuState) and not isinstance(state, InstructionState):
            self.page.floating_action_button = ft.FloatingActionButton(
                icon=ft.icons.HOME, on_click=lambda _: self.transition_to(MainMenuState()), bgcolor=ft.colors.BLUE
            )
        else:
            self.page.floating_action_button = None

        if self.page is not None:
            if len(self.page.controls) > 0:
                self.page.remove_at(0)
            self.page.add(self._state.create_ui())
            self.page.update()

    @staticmethod
    def fetch_product_details(product_name: str, scrapper: ScrapperStrategy, number_of_items=4) -> \
            List[Details]:
        return scrapper.scrape_list_of_products(product_name, number_of_items)

    @staticmethod
    def open_links(links: List[Details]):
        for link in links:
            webbrowser.open(link.details_link)


controller = Controller()
ft.app(controller.run)
