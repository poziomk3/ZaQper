import asyncio
import threading

import flet as ft

from details import Details
from scrapper import fetch_list_of_items, create_driver, fetch_product_details


class MainMenu(ft.UserControl):
    def __init__(self, next_state):
        super().__init__()
        self.next_state = next_state

    def build(self):
        return ft.Column(
            [ft.Text("ZaQ per", text_align=ft.TextAlign.CENTER, size=30),
             ft.Container(content=ft.ElevatedButton(
                 content=ft.Container(content=ft.Text("Lets Go!", text_align=ft.TextAlign.CENTER, size=15), padding=10),
                 on_click=lambda _: self.next_state("list_creator"), bgcolor="blue",
                 animate_size=True,
                 color="white"),
                 padding=ft.Padding(500, 10, 500, 10)),
             ft.Container(content=ft.ElevatedButton(
                 content=ft.Container(content=ft.Text("Learn how it works!", text_align=ft.TextAlign.CENTER, size=15),
                                      padding=10),
                 on_click=lambda _: self.next_state("instruction"), bgcolor="blue",
                 animate_size=True,
                 color="white"),
                 padding=ft.Padding(500, 10, 500, 10))],
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH, height=500)


class Instruction(ft.UserControl):
    def __init__(self, next_state):
        self.next_state = next_state
        super().__init__()

    def build(self):
        return ft.Column(
            [ft.Text("My instruction", text_align=ft.TextAlign.CENTER, size=30), ft.Container(content=ft.ElevatedButton(
                content=ft.Container(content=ft.Text("Go back!", text_align=ft.TextAlign.CENTER, size=15),
                                     padding=10),
                on_click=lambda _: self.next_state("main_menu"), bgcolor="blue",
                animate_size=True,
                color="white"), padding=ft.Padding(500, 10, 500, 10))], alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            height=500)


class ListCreator(ft.UserControl):
    def __init__(self, next_state):
        self.products = []
        super().__init__()
        self.next_state = next_state
        self.view = None
        self.list = ft.Column()
        self.textField = ft.TextField(label="Product you wanna buy!")

    def build(self):
        self.view = ft.Column([ft.Text("ZaQ per", text_align=ft.TextAlign.CENTER, size=30), self.textField,
                               ft.Container(content=ft.ElevatedButton(
                                   content=ft.Container(
                                       content=ft.Text("Add!", text_align=ft.TextAlign.CENTER, size=15),
                                       padding=10),
                                   on_click=self.add_product_to_list, bgcolor="blue",
                                   animate_size=True,
                                   color="white"),
                                   padding=ft.Padding(500, 10, 500, 10)),
                               ft.Container(content=ft.ElevatedButton(
                                   content=ft.Container(
                                       content=ft.Text("Go next!", text_align=ft.TextAlign.CENTER, size=15),
                                       padding=10),
                                   on_click=lambda _: self.next_state("picker"), bgcolor="blue",
                                   animate_size=True,
                                   color="white"),
                                   padding=ft.Padding(500, 10, 500, 10)),
                               ft.Container(ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                                   ft.Column([self.list],
                                             scroll=ft.ScrollMode.ADAPTIVE, width=400
                                             )], height=400),
                                            )],
                              alignment=ft.MainAxisAlignment.CENTER,
                              horizontal_alignment=ft.CrossAxisAlignment.STRETCH, height=500,
                              )
        return self.view

    def add_product_to_list(self, arg: ft.ControlEvent):
        if self.textField.value == "":
            return
        self.products.append(self.textField.value)

        self.list.controls.append(ft.Text(self.textField.value, text_align=ft.TextAlign.CENTER, size=30))
        self.textField.value = ""
        self.update()

    # def go_next(self):
    #     self.controls.remove(self.view)
    #     self.controls.append(ft.Column(
    #         [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
    #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #     ))
    #     self.update()
    #     self.details = fetch_list_of_items(self.products)
    #
    #     self.next_state("product_picker")


class ProductPicker(ft.UserControl):
    def __init__(self, products: list[str]):
        super().__init__()
        print(products)
        self.products = products
        print(products)

    def build(self):
        return ft.Column([ProductRow(prod) for prod in self.products], height=600, scroll=ft.ScrollMode.AUTO,
                         alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # for product in self.products:
        #     self.page.add(ft.SafeArea(ft.Text(product)))


class ProductRow(ft.UserControl):
    def __init__(self, product: str):
        super().__init__()
        self.view = None
        self.number_of_rows = ft.Ref[ft.Dropdown]()
        self.showing_options = ft.Ref[ft.Dropdown]()
        self.product = product
        self.auctions = []

    def build(self):
        self.view = ft.Column([
            ft.Row(
                [
                    ft.Text(self.product.upper(), text_align=ft.TextAlign.CENTER, size=30, font_family="Arial",
                            italic=True),
                    ft.Container(
                        ft.Row([
                            ft.Text("Showing: "),
                            ft.Dropdown(
                                ref=self.number_of_rows,
                                width=60,
                                options=[
                                    ft.dropdown.Option("1"),
                                    ft.dropdown.Option("2"),
                                    ft.dropdown.Option("3"),
                                    ft.dropdown.Option("4"),
                                    ft.dropdown.Option("5"),
                                ],
                                value="1"
                            ), ft.Text("rows.   "),
                            ft.Text("Best options regarding: "),
                            ft.Dropdown(
                                ref=self.showing_options,
                                width=200,
                                options=[
                                    ft.dropdown.Option("Popularity"),
                                    ft.dropdown.Option("Price"),
                                    ft.dropdown.Option("Reviews"),
                                ], value="Popularity"

                            ),
                            ft.ElevatedButton(text="refresh", on_click=lambda _: self.fetch())
                        ],
                            alignment=ft.MainAxisAlignment.END, )
                        , expand=1)],
                alignment=ft.MainAxisAlignment.START)

            , ft.Container()
        ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

        fetch_thread = threading.Thread(target=self.fetch)
        fetch_thread.start()

        return ft.Container(
            self.view, expand_loose=True, expand=True, padding=ft.Padding(10, 10, 10, 40)
        )

    def fetch(self):
        self.view.controls.remove(self.view.controls[1])
        self.view.controls.append(ft.Container(ft.ProgressRing(), padding=ft.Padding(500, 10, 500, 10)))
        self.update()
        driver = create_driver()
        self.auctions = fetch_product_details(self.product, driver)
        self.auctions = [
            Details("makaron sadasd asd aasd sasad", "10", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
            Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
            Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
            Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl"),
            Details("krzyz", "20", "https://picsum.photos/200/300", "https://www.ceneo.pl")]
        self.view.controls.remove(self.view.controls[1])
        # self.inner.controls.append(ft.Container(bgcolor="white", width=200, height=200))
        self.view.controls.append(ft.GridView(
            [ProductDetails(product) for product in self.auctions],
            expand=1,
            runs_count=5,
            max_extent=400,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
            expand_loose=True,

        ))
        self.update()


class ProductDetails(ft.UserControl):
    def __init__(self, product: Details):
        super().__init__()
        self.product = product
        self.view: ft.Container | None = None

    def build(self):
        self.view = ft.Container(
            content=ft.Column([ft.Text(self.product.name, text_align=ft.TextAlign.CENTER, size=10),
                               ft.Container(
                                   ft.Image(src=self.product.image_link, fit=ft.ImageFit.CONTAIN, width=150, height=150
                                            ),
                                   padding=30), ft.Text(self.product.price, text_align=ft.TextAlign.CENTER, size=15), ],
                              horizontal_alignment=ft.CrossAxisAlignment.STRETCH, ),
            aspect_ratio=1.0, padding=10, height=400, width=400, bgcolor="blue", on_click=self.on_click,
        )
        return self.view

    def on_click(self, arg: ft.ControlEvent):
        if self.view.bgcolor == "red":
            self.view.bgcolor = "blue"
            self.scale = 1
        else:
            self.view.bgcolor = "red"
            self.scale = 0.9

        self.update()
