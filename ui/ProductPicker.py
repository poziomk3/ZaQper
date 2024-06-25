import threading
import time

import flet as ft

from model.details import Details
from model.endpoints import get_scrapper_names, get_scrapper_strategy
from model.utils import sortedBy
from scrapper.scrapperList import ScrapperName
from ui.Common import MyButton, MyTitle


class ProductPicker(ft.UserControl):
    def __init__(self, go_next, products: list[str], fetch_details):
        super().__init__()
        self.products = products
        self.go_next = go_next
        self.fetch_details = fetch_details
        self.rows = [ProductRow(prod, self.fetch_details) for prod in self.products]
        print(products)

    def build(self):
        return ft.Column(
            [*self.rows, MyButton("summary", lambda: self.go_next("summary"))], height=760,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def get_clicked(self):
        return [item for sublist in [row.get_is_clicked() for row in self.rows] for item in sublist]


class ProductRow(ft.UserControl):
    def __init__(self, product: str, fetch_details):
        super().__init__()
        self.rows_dd = ft.Ref[ft.Dropdown]()
        self.sort_dd = ft.Ref[ft.Dropdown]()
        self.scrapper_dd = ft.Ref[ft.Dropdown]()
        self.main_column = ft.Ref[ft.Column]()
        self.product_name = product
        self.auctions = []
        self.fetch_details = fetch_details
        self.picked_products = []

    def build(self):
        fetch_thread = threading.Thread(target=self.on_refresh, args=(True,))
        fetch_thread.start()

        return ft.Container(
            ft.Column([
                ft.Row(
                    [
                        MyTitle(self.product_name.upper()),
                        ft.Container(
                            ft.Row([
                                ft.Dropdown(
                                    ref=self.scrapper_dd,
                                    width=140,
                                    options=[ft.dropdown.Option(x) for x in get_scrapper_names()
                                             ],
                                    value=get_scrapper_names()[0]
                                ), ft.Text("Scrapper.   "),
                                ft.Text("Showing: "),
                                ft.Dropdown(
                                    ref=self.rows_dd,
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
                                    ref=self.sort_dd,
                                    width=200,
                                    options=[
                                        ft.dropdown.Option(sortedBy.PRICE_ASC.value),
                                        ft.dropdown.Option(sortedBy.POPULARITY.value),
                                        ft.dropdown.Option(sortedBy.REVIEWS.value),
                                    ], value=sortedBy.POPULARITY.value

                                ),
                                ft.ElevatedButton(text="refresh", on_click=lambda _: self.on_refresh())
                            ],
                                alignment=ft.MainAxisAlignment.END, )
                            , expand=1)],
                    alignment=ft.MainAxisAlignment.START)

                , ft.Container()
            ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH, ref=self.main_column), expand_loose=True,
            expand=True,
            padding=ft.Padding(10, 10, 10, 40)
        )

    def create_spinner(self):
        self.main_column.current.controls.remove(self.main_column.current.controls[1])
        self.main_column.current.controls.append(ft.Container(ft.ProgressRing(), padding=ft.Padding(500, 10, 500, 10)))
        self.update()

    def create_grid(self):
        return ft.GridView(
            [ProductDetails(product) for product in self.auctions],
            expand=1,
            runs_count=5,
            max_extent=400,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
            expand_loose=True,

        )

    def get_is_clicked(self):
        return [auction for index, auction in enumerate(self.auctions) if
                self.main_column.current.controls[1].controls[index].is_clicked]

    def fetch_auctions(self):
        self.auctions = self.fetch_details(self.product_name,
                                           get_scrapper_strategy(ScrapperName(self.scrapper_dd.current.value),
                                                                 self.sort_dd.current.value),
                                           int(self.rows_dd.current.value) * 4)

    def on_refresh(self, init=False):
        if init:
            time.sleep(0.2)
        self.create_spinner()
        self.main_column.current.controls.remove(self.main_column.current.controls[1])
        self.fetch_auctions()
        # self.inner.controls.append(ft.Container(bgcolor="white", width=200, height=200))
        self.main_column.current.controls.append(self.create_grid())

        self.update()


class ProductDetails(ft.UserControl):
    def __init__(self, product: Details):
        super().__init__()
        self.product = product
        self.view: ft.Container | None = None
        self.is_clicked = False

    def build(self):
        self.view = ft.Container(
            content=ft.Column([ft.Text(self.product.name, text_align=ft.TextAlign.CENTER, size=13),
                               ft.Container(
                                   ft.Image(src=self.product.image_link, fit=ft.ImageFit.CONTAIN, width=150, height=100
                                            ),
                                   padding=30),
                               ft.Text(self.product.price + " PLN", text_align=ft.TextAlign.CENTER, size=15,
                                       weight=ft.FontWeight.W_700), ],
                              horizontal_alignment=ft.CrossAxisAlignment.STRETCH, ),
            aspect_ratio=1.0, padding=10, height=400, width=400, on_click=self.on_click,
            border=ft.Border(ft.BorderSide(5, "white"), ft.BorderSide(5, "white"), ft.BorderSide(5, "white"),
                             ft.BorderSide(5, "white"))
        )
        return self.view

    def on_click(self, arg: ft.ControlEvent):
        if self.view.scale == 0.7:
            self.view.scale = 1
            self.is_clicked = False
        else:
            self.view.scale = 0.7
            self.is_clicked = True

        self.update()
