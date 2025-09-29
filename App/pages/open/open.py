import flet as ft
from tkinter import Tk, filedialog
from App.storage import app_state
import App.router as rout
import os
from pathlib import Path
from App.src.projectsControl.DataControl import start_getinfo
from App.src.projectsControl.DataControl import saveChange

from App.pages.open.control import ProjManageContainer



def open_directory_dialog():
    # Создаем скрытое окно Tkinter
    root = Tk()
    root.withdraw()  # Скрываем основное окно
    root.attributes('-topmost', True)  # Поверх других окон
    
    # Открываем диалог выбора директории
    directory = filedialog.askdirectory(title="Выберите папку")
    

    if directory:  # Если папка выбрана
        app_state.project_name = directory.split('/')[-1]
        Path(f"./UserData/projects/{app_state.project_name}").mkdir(parents=True, exist_ok=True)

        app_state.global_path = directory
        app_state.files = [f for f in os.listdir(directory) if f.endswith('.mkv')]
        start_getinfo()
        saveChange()
        app_state.new_page(rout.Editor)
        


def project_header():
    buttonList = []
    buttonList.append(ft.ElevatedButton('Создать новый проект', on_click=lambda e: open_directory_dialog()))

    for project in app_state.projects:
        buttonList.append(ProjManageContainer(project))

    return buttonList
    






def projects_library():
    return ft.Column([
            ft.Text("Откройте сохраненный проект или создайте новый!", size=20, weight='bold'),
            ft.Column(project_header())
        ],        
        expand=True,
        spacing=20
    )


def projects_manage():
    Path(f"./UserData/projects").mkdir(parents=True, exist_ok=True)
    app_state.projects = [f for f in os.listdir('./UserData/projects')]
    return projects_library()
    


    
        

