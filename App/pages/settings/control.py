import flet as ft


class OptionButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.text = text