import flet as ft

def converter():
    return ft.Column(
        controls=[
            ft.Text('Конвертер', size=20)
        ],
        expand=True,
        spacing=20,
    )
