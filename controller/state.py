from abc import ABC, abstractmethod
from typing import Optional, List

from ui import MainMenu, ListCreator, ProductPicker, Instruction, Summary
import flet as ft


class State(ABC):
    context = None

    @abstractmethod
    def go_to_next_state(self, additional_info: str) -> None:
        pass

    @abstractmethod
    def create_ui(self) -> ft.UserControl:
        pass


class MainMenuState(State):
    def go_to_next_state(self, additional_info):
        if additional_info == "instruction":
            self.context.transition_to(InstructionState())
        elif additional_info == "list_creator":
            self.context.transition_to(ListCreatorState())

    def create_ui(self):
        return MainMenu(self.go_to_next_state)


class InstructionState(State):
    def go_to_next_state(self, additional_info):
        self.context.transition_to(MainMenuState())

    def create_ui(self):
        return Instruction(self.go_to_next_state)


class ListCreatorState(State):
    def __init__(self):
        self.view: Optional[ProductPicker] = None

    def go_to_next_state(self, additional_info):
        state = ProductPickerState()
        state.products = self.view.products

        self.context.transition_to(state)

    def create_ui(self):
        self.view = ListCreator(self.go_to_next_state)
        return self.view


class ProductPickerState(State):

    def __init__(self):
        self.view: Optional[ProductPicker] = None
        self.products: List[str] = []

    def go_to_next_state(self, additional_info):
        products = self.view.get_clicked()
        self.context.open_links(products)
        new_state = SummaryState()
        new_state.products = products
        self.context.transition_to(new_state)

    def create_ui(self):
        self.view = ProductPicker(self.go_to_next_state, self.products, self.context.fetch_product_details)
        return self.view


class SummaryState(State):

    def __init__(self):
        self.products = []

    def go_to_next_state(self, additional_info):
        self.context.transition_to(MainMenuState())

    def create_ui(self):
        return Summary(self.go_to_next_state, self.products)
