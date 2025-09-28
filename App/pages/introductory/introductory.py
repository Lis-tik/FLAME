import flet as ft
from App.storage import app_state


def introductory():
    return ft.Column(
        controls=[
            ft.Text('Добро пожаловать в FLAME', size=20, weight='bold'),
            ft.TextButton(
                content=ft.Text(
                    "Официальный GitHub разработчика",
                    color="blue",
                    size=15
                ),
                on_click=lambda e: app_state.page_control.launch_url("https://github.com/Lis-tik/muxon"),
                style=ft.ButtonStyle(padding=0)  
            )
        ],
        expand=True,
        spacing=20,
    )

