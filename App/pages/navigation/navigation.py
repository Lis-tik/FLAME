from App.storage import app_state
import flet as ft
import App.router as rout



def navigation():
    return ft.Row(
        controls=[
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.HOME, size=16),
                    ft.Text("Главная", size=14),
                ], spacing=8),
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    shape=ft.RoundedRectangleBorder(radius=6),
                ),
                on_click=lambda e: app_state.new_page(rout.Introductory),
            ),
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.MENU, size=16),
                    ft.Text("Менеджер проектов", size=14),
                ], spacing=8),
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    shape=ft.RoundedRectangleBorder(radius=6),
                ),
                on_click=lambda e: app_state.new_page(rout.Projects),
            ),
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.DRIVE_FILE_RENAME_OUTLINE, size=16),
                    ft.Text("Редактор профиля", size=14),
                ], spacing=8),
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    shape=ft.RoundedRectangleBorder(radius=6),
                ),
                on_click=lambda e: app_state.new_page(rout.Editor),
            ),
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.SYNC, size=16),
                    ft.Text("Процесс", size=14),
                ], spacing=8),
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    shape=ft.RoundedRectangleBorder(radius=6),
                ),
                on_click=lambda e: app_state.new_page(rout.monitoring),
            ),
        ],
        spacing=8,
        run_spacing=8,
        alignment=ft.MainAxisAlignment.START,
    )