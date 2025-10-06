import flet as ft
from App.pages.converter.control import createProfile, profileButton, BashInput
from App.storage import app_state
from App.src.convertedition.DataControl import initialization_profiles



def convertEdit():
    return ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('')
            ])
        ])
    )


def retCol():
    content = []
    for index, prof in enumerate(app_state.CONVERT_PROFILES):
        content.append(profileButton(prof))

    return ft.Column(content)



def summaryData():
    if not app_state.viewed_profile:
        return ft.Text('Выберете или создайте профиль для редактирования')
    
    return ft.Container(
        BashInput()
    )



def main():
    return ft.Row([
        ft.Column([
            createProfile(),
            ft.Divider(height=1),
            retCol()
        ], expand=1),

        ft.Column([
            summaryData()
        ], expand=4)
    ], expand=True)


def converter():
    initialization_profiles()
    return ft.Container(
        main()
    )