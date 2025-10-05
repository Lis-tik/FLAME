import flet as ft
from App.storage import app_state
import App.router as rout 


class profileButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__(expand=True)
        self.text = text
        # self.on_click = self.modeFunc


        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            # bgcolor=(ft.Colors.GREY_300 if self.viewed else ft.Colors.WHITE)
            )
    




class createProfile(ft.ElevatedButton):
    def __init__(self):
        super().__init__(expand=True)
        self.text = 'Создать новый профиль'
        self.on_click = self.func

        self.content = ft.Column(
            controls=[
                ft.Text(self.text, size=15),
                # ft.Text(_uid, size=10, color=ft.Colors.GREY),
            ],
            spacing=0,
            tight=True
        )

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            # bgcolor=(ft.Colors.GREY_300 if self._uid == app_state.EditorPage.viewed_uid else ft.Colors.WHITE),
        )

    def func(self, e):
        return
        app_state.new_page(rout.Editor)
