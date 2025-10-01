import flet as ft
from App.storage import app_state
import App.router as rout
from App.pages.editor.control import UnificationButton, RuleButton, EditingInput, SampleMode, StatusCheck, StatusMediaFlag, ModeButton, addTrack, LangDrop, actTrack
from App.src.projectsControl.DataControl import saveChange


def modeCheck():
    if app_state.EditorPage.info_mode == 'general':
        return ft.Text('Общие сведения')
    
    if app_state.EditorPage.viewed_uid in app_state.EditorPage.mediainfo[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode]:
        app_state.EditorPage.viewed_track = app_state.EditorPage.mediainfo[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid]
    else:
        app_state.EditorPage.viewed_uid = None

    if not app_state.EditorPage.viewed_uid:
        return ft.Text('Необходимо выбрать дорожку')
    
    if app_state.EditorPage.info_mode == 'audio':
        return audioChannel()
    elif app_state.EditorPage.info_mode == 'subtitle':
        return subtitleChannel()
    elif app_state.EditorPage.info_mode == 'video':
        return videoChannel()


    
def GeneralInfo():
    return ft.Text("Тут будет общая информация")

def videoChannel():
    return ft.Container(
        ft.Column([
            ft.Text('Общие сведения и метаданные', size=18, weight='bold'),
            ft.Row([
                ft.Text(f"Разрешение сторон:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['width']}x{app_state.EditorPage.viewed_track['height']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Кодек:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['codec_name']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Профиль:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['profile']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"fps:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['r_frame_rate']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Битрейт:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['bit_rate']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Количество кадров:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['nb_frames']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Тип цветопередачи:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['pix_fmt']}", size=15),
            ]),

            ft.Divider(height=1),


            ft.Text('Параметры конвертера', size=18, weight='bold'),
            ft.ElevatedButton('Доступные профили')
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(app_state.EditorPage.viewed_track['status']) else ft.Colors.BLACK12
    )


def subtitleChannel():
    return ft.Container(
        ft.Column([
            ft.Row([
                ft.Text("Описание (имя) субтитров:", size=15, weight='bold'),
                EditingInput()
            ]),
            ft.Row([
                ft.Text(f"Язык субтитров:", size=15, weight='bold'),
                LangDrop(app_state.EditorPage.viewed_track['language']),
            ]),
            ft.Row([
                ft.Text(f"Формат:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['format']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Источник:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['path'] if app_state.EditorPage.viewed_track['path'] else '[в составе контейнера]'}", size=15),
            ]),
            ft.Divider(height=1),

            ft.Text('Параметры конвертера', size=18, weight='bold'),
            ft.ElevatedButton('Доступные профили')
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(app_state.EditorPage.viewed_track['status']) else ft.Colors.BLACK12
    )



def audioChannel():
    return ft.Container(
        ft.Column([
            ft.Row([
                ft.Text("Описание (имя) аудиодорожки:", size=15, weight='bold'),
                EditingInput()
            ]),
            ft.Row([
                ft.Text(f"Индекс в контейнере:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['index']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Язык аудиодорожки:", size=15, weight='bold'),
                LangDrop(app_state.EditorPage.viewed_track['language']),
            ]),
            ft.Row([
                ft.Text(f"Кодек аудиодорожки:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['codec_name']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Количество каналов:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['channels']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Битрейт:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['bit_rate']}", size=15),
            ]),
            ft.Row([
                ft.Text(f"Источник:", size=15, weight='bold'),
                ft.Text(f"{app_state.EditorPage.viewed_track['path'] if app_state.EditorPage.viewed_track['path'] else '[в составе контейнера]'}", size=15),
            ]),
            ft.Divider(height=1),

            ft.Text('Параметры конвертера', size=18, weight='bold'),
            ft.ElevatedButton('Доступные профили')
        ]),
        bgcolor=ft.Colors.TRANSPARENT if int(app_state.EditorPage.viewed_track['status']) else ft.Colors.BLACK12
    )



def includedButton():
    filesMain = []
    filesMain.append(UnificationButton('Режим объединения (BETA)'))
    filesMain.append(SampleMode())
    
    if app_state.EditorPage.mediainfo:
        for file in app_state.EditorPage.mediainfo:
            loop = ft.Row([
                StatusCheck(file),
                RuleButton(file)
            ])
            filesMain.append(loop)

    return filesMain




def Information():
    return ft.Row(
        controls=[                    
            # Левый блок - список файлов (1/4)
            ft.Container(
                content=ft.Column(
                    controls=includedButton(),
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                ),
                expand=1,  # 1 часть из 4
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=10,
                padding=10,
                margin=ft.margin.symmetric(vertical=10),
            ),
            # Правый блок - метаданные (3/4)
            metaData()
        ],
        expand=True,
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

def metaData():
    return ft.Container(
        content=ft.Column([
            ft.Divider(height=1),
            ft.Row(   # кнопки сверху
                [
                    ModeButton("Общее", 'general'),
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
        expand=3,
    )

def distributionData():
    if not app_state.EditorPage.viewed_files:
        return ft.Container(
            content=ft.Row([ft.Text("Выберете файл для просмотра информации", size=15)])
        )
    
    content=[]
    if app_state.EditorPage.info_mode != "general":
        content.append(addTrack())
        for tracks in app_state.EditorPage.mediainfo[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode]:
            track = ft.Row([
                StatusMediaFlag(str(tracks)),
                actTrack(str(tracks))
            ])
            content.append(track)



    return ft.Container(
        ft.Row([
            ft.Column(content, expand=1),
            ft.Column([modeCheck()], expand=3)
        ], 
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.START)
    )



def get_editor_page():
    return ft.Column(
        controls=[
            ft.Text(app_state.viewed_project, size=20, weight='bold'),
            Information()
        ],
        expand=True,
        spacing=20,
    )

