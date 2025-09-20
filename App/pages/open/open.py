import flet as ft
from tkinter import Tk, filedialog
from App.storage import app_state
import App.router as rout
import os
from pathlib import Path
from App.src.media_info import start_getinfo



def open_directory_dialog():
    # Создаем скрытое окно Tkinter
    root = Tk()
    root.withdraw()  # Скрываем основное окно
    root.attributes('-topmost', True)  # Поверх других окон
    
    # Открываем диалог выбора директории
    directory = filedialog.askdirectory(title="Выберите папку")
    

    if directory:  # Если папка выбрана
        app_state.project_name = directory.split('/')[-1]
        Path(f"./projects/{app_state.project_name}/data.json").mkdir(parents=True, exist_ok=True)

        app_state.global_path = directory
        app_state.files = [f for f in os.listdir(directory) if f.endswith('.mkv')]
        start_getinfo()
        app_state.new_page(rout.Editor)
        


def project_header():
    buttonList = []
    buttonList.append(ft.ElevatedButton('Создать новый проект', on_click=lambda e: open_directory_dialog()))

    for project in app_state.projects:
        proj = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.SETTINGS, size=24, color=ft.Colors.BLUE_700),
                    ft.Column(
                        controls=[
                            ft.Text(project, 
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
            ), 
            padding=ft.padding.all(15),
            # bgcolor=ft.Colors.GREY_100,
            # width=float("inf"),
            border=ft.border.only(bottom=ft.border.BorderSide(1, ft.Colors.GREY_300)),
        )
        buttonList.append(proj)
    return buttonList
    






def projects_library():
    return ft.Column([
            ft.Text("Откройте сохраненный проект или создайте новый!", size=16),
            ft.Column(project_header())
        ],        
        expand=True,
        spacing=20
    )


def projects_manage():
    Path(f"./projects").mkdir(parents=True, exist_ok=True)
    app_state.projects = [f for f in os.listdir('./projects')]
    return projects_library()
    


    
        

