import flet as ft
from App.pages.monitoring.control import startConvert

def monitoring():
    return ft.Container(
        startConvert()
    )