from typing import List

import flet as ft

from controller.state import State, MainMenuState
from model.details import Details
from model.scrapperStrategies import ScrapperStrategy
import webbrowser


class Controller:

    def __init__(self):
        self.state = None
        self.page = None
        print("Controller created")

    def run(self, page: ft.Page):
        self.page = page
        self.page.window_width = 1400
        self.page.window_height = 800
        self.page.window_resizable = False
        self.transition_to(MainMenuState())
        self.page.update()

    def transition_to(self, state: State):
        self.state = state
        self.state.context = self
        if not isinstance(state, MainMenuState):
            self.page.floating_action_button = ft.FloatingActionButton(
                icon=ft.icons.HOME, on_click=lambda _: self.transition_to(MainMenuState()), bgcolor=ft.colors.BLUE
            )
        else:
            self.page.floating_action_button = None

        if self.page is None:
            return

        if len(self.page.controls) > 0:
            self.page.remove_at(0)
        self.page.add(self.state.create_ui())
        self.page.update()

    @staticmethod
    def fetch_product_details(product_name: str, scrapper: ScrapperStrategy, number_of_items=4) -> \
            List[Details]:
        return scrapper.scrape_list_of_products(product_name, number_of_items)

    @staticmethod
    def open_links(links: List[Details]):
        for link in links:
            webbrowser.open(link.details_link)


