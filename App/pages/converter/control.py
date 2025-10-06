import flet as ft
from App.storage import app_state
import App.router as rout 


class BashInput(ft.TextField):
    def __init__(self, initial_value=""):
        super().__init__(expand=True)
        self.value = initial_value


class profileButton(ft.ElevatedButton):
    def __init__(self, data):
        super().__init__(expand=True)
        self.data = data
        self.text = data['name']
        self.on_click = self.profile
        self.viewed = True if self.data == app_state.viewed_profile else False


        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if self.viewed else ft.Colors.WHITE)
            )
        
    def profile(self, e):
        app_state.viewed_profile = self.data
        app_state.new_page(rout.Converter)
    




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
        app_state.new_page(rout.Converter)
