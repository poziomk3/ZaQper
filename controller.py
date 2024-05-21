import flet as ft

from details import Details
from ui import ProductPicker
from scrapper import fetch_list_of_items


# Define Controller class

class Controller:
    def __init__(self):
        self.page = None
        self.product_picker = ProductPicker([])

    def run(self, page: ft.Page):
        self.page = page
        self.update()  # Call update initially
        page.add(ft.Column([ft.Text("zaQper"), self.product_picker],
                           alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def update(self):
        list_of_items = fetch_list_of_items(["makaro`n", "krzyz"])
        self.product_picker = ProductPicker(list_of_items)
        # self.product_picker = ProductPicker([[Details("makaron sadasd asd aasd sasad", "10", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
        #                                       Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl")],
        #                                      [Details("makaron", "10", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
        #                                       Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl")]])
        self.page.update()


# Create an instance of Controller
controller = Controller()

# Run the application with the controller's run method
ft.app(controller.run)

# Update the controller to fetch new items
