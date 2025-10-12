
import flet as ft
from App.src.convertedition.process import start
from App.src.projectsControl.DataControl import saveChange



class startConvert(ft.ElevatedButton):
    def __init__(self):
        super().__init__(expand=True)
        self.text = 'Запуск'
        self.on_click = self.tracknum

    def tracknum(self, e):
        saveChange()
        start()
