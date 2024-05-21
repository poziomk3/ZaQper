import flet as ft

from details import Details
from state import MainMenuState, State
from ui import ProductPicker, MainMenu, ListCreator
from scrapper import fetch_list_of_items


# Define Controller class

class Controller:
    _state = None
    page = None

    def __init__(self):
        print("Controller created")

    def run(self, page: ft.Page):
        self.page = page
        self.transition_to(MainMenuState())
        # page.add(ft.Column([ft.Text("zaQper"), self.product_picker],
        #                    alignment=ft.MainAxisAlignment.CENTER))

        page.update()

    def update(self):
        list_of_items = fetch_list_of_items(["makaron", "krzyz"])
        self.product_picker = ProductPicker(list_of_items)
        # self.product_picker = ProductPicker([[Details("makaron sadasd asd aasd sasad", "10", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
        #                                       Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl")],
        #                                      [Details("makaron", "10", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
        #                                       Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl")]])
        self.page.update()

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
        if self.page is not None:
            if len(self.page.controls) > 0:
                self.page.remove_at(0)
            self.page.add(self._state.create_ui())
            self.page.update()


# Create an instance of Controller
controller = Controller()

# Run the application with the controller's run method
ft.app(controller.run)

# Update the controller to fetch new items
