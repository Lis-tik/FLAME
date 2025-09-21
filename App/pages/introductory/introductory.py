import flet as ft



def introductory():
    return ft.Column(
        controls=[
            ft.Text('Добро пожаловать в FLAME', size=20, weight='bold'),
            ft.Text(
                "Посетите наш сайт", 
                color="blue", 
                style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                # on_click=lambda e: page.launch_url("https://example.com")
            )
        ],
        expand=True,
        spacing=20,
    )

