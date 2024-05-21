from abc import ABC, abstractmethod
import flet as ft

from ui import MainMenu, ListCreator, ProductPicker, Instruction


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def go_to_next_state(self, additional_info: str):
        pass

    @abstractmethod
    def create_ui(self):
        pass


class MainMenuState(State):
    def go_to_next_state(self, additional_info) -> None:
        if additional_info == "instruction":
            self.context.transition_to(InstructionState())
        elif additional_info == "list_creator":
            self.context.transition_to(ListCreatorState())

    def create_ui(self):
        return MainMenu(self.go_to_next_state)


class ListCreatorState(State):
    def go_to_next_state(self, additional_info) -> None:
        print("change to list product_picker")
        self.context.transition_to(ProductPickerState())

    def create_ui(self):
        return ListCreator([])


class ProductPickerState(State):
    def go_to_next_state(self, additional_info) -> None:
        print("change to main menu")
        self.context.transition_to(MainMenuState())

    def create_ui(self):
        return ProductPicker([])


class InstructionState(State):
    def go_to_next_state(self, additional_info) -> None:
        print("change to main menu")
        self.context.transition_to(MainMenuState())

    def create_ui(self):
        return Instruction(self.go_to_next_state)
