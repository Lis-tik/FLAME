import flet as ft
from tkinter import Tk, filedialog
from App.storage import app_state
import App.router as rout
import os
from pathlib import Path



def open_directory_dialog():
    # Создаем скрытое окно Tkinter
    root = Tk()
    root.withdraw()  # Скрываем основное окно
    root.attributes('-topmost', True)  # Поверх других окон
    
    # Открываем диалог выбора директории
    directory = filedialog.askdirectory(title="Выберите папку")

    if directory:  # Если папка выбрана
        app_state.global_path = directory
        app_state.files = [f for f in os.listdir(directory) if f.endswith('.mkv')]
        app_state.new_page(rout.Page_Home)
        





def projects_library(projects):
    buttonList = []
    for project in projects:
        butLi = ft.ElevatedButton(
            project,
            on_click=lambda e: open_directory_dialog(), 
        )
        buttonList.append(butLi)
    buttonList.append(ft.ElevatedButton('Создать новый проект', on_click=lambda e: open_directory_dialog()))

    return ft.Column([
            ft.Text(f"Добро пожаловать в FLAME", size=30, weight="bold"),
            ft.Text("Откройте сохраненный проект или создайте новый!", size=16),
            ft.Row(buttonList)
        ])

def create_project():
    return ft.Column(
        controls=[
            ft.Text(f"Добро пожаловать в FLAME", size=30, weight="bold"),
            ft.Text("Создайте свой первый проект!", size=16),
            ft.ElevatedButton(
                "Создать +",
                on_click=lambda e: open_directory_dialog(), 
            ),
        ],
        alignment="center",
        horizontal_alignment="center",
    )


def projects_manage():
    Path('./projectslib').mkdir(exist_ok=True)
    projects = [f for f in os.listdir('./projectslib')]
    if projects:
        return projects_library(projects)
    
    return create_project()


    
        

