import flet as ft
import App.router as rout
from App.src.projectsControl.DataControl import unpackingData
from App.storage import app_state

class ProjManageContainer(ft.Container):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.EDIT, size=24, color=ft.Colors.BLUE_700),
                ft.Column(
                    controls=[
                        ft.Text(self.data, 
                            size=18, 
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK87),

                        ft.Text("Последнее изменение: ", 
                            size=12, 
                            color=ft.Colors.GREY_600),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        )
        self.padding=ft.padding.all(15)
        self.border=ft.border.only(bottom=ft.border.BorderSide(1, ft.Colors.GREY_300))
        self.on_click = self.projectRule

    def projectRule(self, e):
        app_state.viewed_project = self.data
        unpackingData(self.data)
        app_state.new_page(rout.Editor)