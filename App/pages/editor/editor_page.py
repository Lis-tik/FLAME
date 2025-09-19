import flet as ft
from App.storage import app_state
import App.router as rout
from App.pages.editor.control import UnificationButton, RuleButton, EditingInput, SampleMode, StatusCheck, StatusMediaFlag, ModeButton, addTrack

        

def videoChannel(state):
    return ft.Container(
        ft.Column([
            # StatusMediaFlag(index),
            ft.Row([
                ft.Text(f"Разрешение сторон:", size=15, weight='bold'),
                ft.Text(f"{state['width']}x{state['height']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Тип цветопередачи:", size=15, weight='bold'),
                ft.Text(f"{state['pix_fmt']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Профиль:", size=15, weight='bold'),
                ft.Text(f"{state['profile']}", size=15),
            ]),
            ft.Divider(height=1)
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(state['status']) else ft.Colors.BLACK12
    )


def subtitleChannel(state, index):
    return ft.Container(
        ft.Column([
            StatusMediaFlag(index),
            ft.Row([
                ft.Text("Описание (имя) субтитров:", size=15, weight='bold'),
                EditingInput(state['title'], index, 'subtitle')
            ]),
            ft.Row([
                ft.Text(f"Язык субтитров:", size=15, weight='bold'),
                ft.Text(f"{state['language']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Формат:", size=15, weight='bold'),
                ft.Text(f"{state['format']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Источник:", size=15, weight='bold'),
                ft.Text(f"{state['path'] if state['path'] else '[в составе контейнера]'}", size=15),
            ]),
            ft.Divider(height=1)
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(state['status']) else ft.Colors.BLACK12
    )



def audioChannel(state, index):
    return ft.Container(
        ft.Column([
            StatusMediaFlag(index),
            ft.Row([
                ft.Text("Описание (имя) аудиодорожки:", size=15, weight='bold'),
                EditingInput(state['title'], index, 'audio')
            ]),
            ft.Row([
                ft.Text(f"Индекс в контейнере:", size=15, weight='bold'),
                ft.Text(f"{state['index']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Язык аудиодорожки:", size=15, weight='bold'),
                ft.Text(f"{state['language']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Кодек аудиодорожки:", size=15, weight='bold'),
                ft.Text(f"{state['codec_name']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Количество каналов:", size=15, weight='bold'),
                ft.Text(f"{state['channels']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Битрейт:", size=15, weight='bold'),
                ft.Text(f"{state['bit_rate']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Источник:", size=15, weight='bold'),
                ft.Text(f"{state['path'] if state['path'] else '[в составе контейнера]'}", size=15),
            ]),
            ft.Divider(height=1)
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(state['status']) else ft.Colors.BLACK12
    )



def includedButton():
    filesMain = []
    filesMain.append(UnificationButton('Режим объединения (BETA)'))
    filesMain.append(SampleMode())
    
    for file in app_state.files:
        loop = ft.Row([
            StatusCheck(file),
            RuleButton(file)
        ])
        filesMain.append(loop)

    return filesMain




def Information():
    return ft.Row(
        controls=[                    
            # Правый блок - список файлов
            ft.Column(
                controls = [
                    ft.Container(
                        content=ft.Column(
                            controls=includedButton(),
                            spacing=10,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        expand=True,  # Занимает вторую половину ширины Row
                        border=ft.border.all(1, ft.Colors.GREY_400),
                        border_radius=10,
                        padding=10,
                        margin=ft.margin.symmetric(vertical=10),
                    ),
                ]
            ),
            metaData()
        ],
        expand=True,  # Row растягивается на всю доступную ширину
        spacing=10,   # Расстояние между блоками
        vertical_alignment=ft.CrossAxisAlignment.START  # ← Ключевой параметр!
    )

def metaData():
    
    def modecheck():
        container = []
        if not app_state.EditorPage.viewed_files:
            container.append(ft.Row([
                ft.Text('Информация: ', size=15, weight='bold')
                ], alignment="spaceBetween"))
        else:
            for x in app_state.EditorPage.viewed_files:
                container.append(ft.Row([
                    ft.Text(f'{x}', size=15, weight='bold'),
                    ft.Text('Status:', size=13)
                ], alignment="spaceBetween"))

        return ft.Column(container)
    
    
    return ft.Container(
        content=ft.Column([
            modecheck(),
            ft.Divider(height=1),
            ft.Row(   # кнопки сверху
                [
                    ModeButton("Видео", 'video'),
                    ModeButton("Аудио", 'audio'),
                    ModeButton("Субтитры", 'subtitle')
                ],
                alignment="start",
            ),
            ft.Divider(height=1),
            distributionData()
        ],
        scroll=ft.ScrollMode.AUTO,
        ),
        padding=20,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=2),
        expand=True,  # Занимает половину ширины Row
    )

def distributionData():
    if not app_state.EditorPage.viewed_files:
        return ft.Container(
            content=ft.Row([ft.Text("Выберете файл для просмотра информации", size=15)])
        )
    
    # elif app_state.EditorPage.unification_mode:
    #     return ft.Container(
    #         content=ft.Row([
    #             ft.Text("Вы в режиме объединения файлов", size=15),
    #             ft.Text(f'{app_state.EditorPage.viewed_files}')
    #             ])
    #     )
    
    info_page = []

    info_page.append(addTrack())
    info_page.append(ft.Divider(height=1))



    

    for index, state in enumerate(app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode]):
        if app_state.EditorPage.info_mode == 'audio':
            textField = audioChannel(state, index)

        elif app_state.EditorPage.info_mode == 'video':
            textField = videoChannel(state)
        
        elif app_state.EditorPage.info_mode == 'subtitle':
            textField = subtitleChannel(state, index)
                

        info_page.append(textField)


    return ft.Column(info_page)





def navigation():
    return ft.Row(  # Лучше адаптируется для мобильных устройств
        controls=[
            ft.ElevatedButton(
                "Главная",
                on_click=lambda e: app_state.new_page(rout.Page_Open),
            ),
            ft.ElevatedButton(
                "Входные данные", 
                on_click=lambda e: app_state.new_page(rout.Page_setting_converter),
            ),
            ft.ElevatedButton(
                "Конвертер",
                on_click=lambda e: app_state.new_page(rout.multipage(3)),
            ),
            ft.ElevatedButton(
                "Выходные данные",
                on_click=lambda e: app_state.new_page(rout.multipage(4)),
            ),
        ],
        spacing=10,
        run_spacing=10,  # Перенос на новую строку при нехватке места
    )

def Label():
    return ft.Container(
        content=ft.Text("FLAME", size=30, weight='bold'),
        padding=5,
    )

def get_editor_page():
    return ft.Column(
        controls=[
            Label(),
            navigation(),
            Information(),
        ],
        expand=True,
        spacing=20,
    )

