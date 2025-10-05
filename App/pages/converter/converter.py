import flet as ft
from App.pages.converter.control import createProfile, profileButton
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
    for prof in app_state.CONVERT_PROFILES:
        content.append(profileButton(prof['name']))

    return ft.Column(content)

        

def main():
    return ft.Row([
        ft.Column([
            createProfile(),
            ft.Divider(height=1),
            retCol()
        ], expand=1),

        ft.Column([
            ft.Text('Какие-то настройки профился')
        ], expand=4)
    ], expand=True)


def converter():
    initialization_profiles()
    return ft.Container(
        main()
    )