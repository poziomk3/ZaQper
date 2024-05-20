import flet as ft
from productPicker import ProductPicker


def main(page: ft.Page):
    page.add(ProductPicker(["szminka", "szampon", "pasta do zębów"]))
    page.update()


ft.app(main)
