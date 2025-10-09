import flet as ft
from App.pages.converter.control import createProfile, profileButton, BashInput
from App.storage import app_state
from App.src.convertedition.DataControl import initialization_profiles



def convertEdit():
    return ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('Имя профиля: ', size=15, weight='bold'),
                ft.Text(app_state.viewed_profile['name'], size=15)
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
    
    return convertEdit()



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

    return ft.Container(
        main()
    )