import time
from typing import List

import flet as ft

from details import Details
from scrapperStrategies import ScrapperStrategy, create_driver
from state import MainMenuState, State
import webbrowser


class Controller:
    _state = None
    page = None

    def __init__(self):
        print("Controller created")

    def run(self, page: ft.Page):
        self.page = page
        self.transition_to(MainMenuState())
        page.update()

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")

        self._state = state
        self._state._context = self
        if not isinstance(state, MainMenuState):
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
