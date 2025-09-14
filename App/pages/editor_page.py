import flet as ft
from App.storage import app_state
import App.router as rout
from tkinter import Tk, filedialog
import os




class UnificationButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.on_click = self.enable_unification_mode

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if app_state.EditorPage.unification_mode else ft.Colors.WHITE)
        )

    def enable_unification_mode(self, e):
        app_state.EditorPage.unification_mode = not(app_state.EditorPage.unification_mode)
        app_state.new_page(rout.Page_Home)


class RuleButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.on_click = self.modeFunc

        self.viewed = True if app_state.EditorPage.viewed_file == self.text else False

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if self.viewed else ft.Colors.WHITE)
            )
    
    def modeFunc(self, e):
        app_state.EditorPage.viewed_file = self.text
        app_state.new_page(rout.Page_Home)
        


class EditingInput(ft.TextField):
    def __init__(self, value, index, mode):
        super().__init__()
        self.value = value
        self.mode = mode 
        self.index = index
        self.border_color = ft.Colors.BLUE if self.value else ft.Colors.RED
        self.hint_text = 'Поле должно быть заполнено!'
        self.on_change = self.handle_change

    
    def handle_change(self, e):
        app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_file][self.mode][self.index]['title'] = self.value
        print(f"Новый текст: {self.value}")
        
        if not self.value:
            self.border_color = ft.Colors.RED
        else:
            self.border_color = ft.Colors.BLUE
        self.update()


class SampleMode(ft.Checkbox):
    def __init__(self):
        super().__init__()
        self.label = 'Убрать все выделенные файлы' #if (len(app_state.activeFilesHome) > 0) else 'Выделить все файлы'
        # self.on_change = self.SampleModeFunc

        self.value = False #if (len(app_state.mediainfo_Copy) == len(app_state.files)) else False

    def SampleModeFunc(self, e):
        for qulT in app_state.files:
            if not (len(app_state.activeFilesHome) == len(app_state.files)):
                app_state.activeFilesHome.append(qulT) 
                continue
            app_state.activeFilesHome.clear() 
            break

        app_state.new_page(rout.Page_Home)


class StatusCheck(ft.Checkbox):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.on_change = self.SampleModeFunc
        self.value = bool(app_state.EditorPage.mediainfo_copy[self.file]['status']) 

    def SampleModeFunc(self, e):
        app_state.EditorPage.mediainfo_copy[self.file]['status'] = int(not(app_state.EditorPage.mediainfo_copy[self.file]['status']))
        app_state.new_page(rout.Page_Home)


        
        

class ModeButton(ft.ElevatedButton):
    def __init__(self, text, mode):
        super().__init__()
        self.text = text
        self.mode = mode
        self.on_click = self.infoModeTool

        self.active = True if app_state.EditorPage.info_mode == self.mode else False

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if self.active else ft.Colors.WHITE)
            )
    

    def infoModeTool(self, e):
        app_state.EditorPage.info_mode = self.mode
        app_state.new_page(rout.Page_Home)





        
        

def videoChannel(state):
    return ft.Column([
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
    ])


def subtitleChannel(state, index):
    return ft.Column([
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
    ])



def audioChannel(state, index):
    return ft.Column([
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
    ])



def includedButton():
    filesMain = []
    filesMain.append(UnificationButton('Режим объединения (BETA)'))
    filesMain.append(SampleMode())
    
    for file in app_state._files:
        loop = ft.Row([
            StatusCheck(file),
            RuleButton(file)
        ])
        filesMain.append(loop)

    return filesMain





def open_directory_dialog():
    root = Tk()
    root.withdraw()  # Скрываем основное окно
    root.attributes('-topmost', True)  # Поверх других окон
    
    # Открываем диалог выбора директории
    directory = filedialog.askdirectory(title="Выберите папку")

    if directory:  # Если папка выбрана
        app_state.global_path = directory
        app_state.files = [f for f in os.listdir(directory)]


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
    return ft.Container(
        content=ft.Column([
            ft.Text(app_state.EditorPage.viewed_file if app_state.EditorPage.viewed_file else 'Информация', size=20, weight='bold'),
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
    if not app_state.EditorPage.viewed_file:
        return ft.Container(
            content=ft.Row([ft.Text("Выберете файл для просмотра информации", size=15)])
        )
    
    info_page = []

    info_page.append(ft.Text(f"Статус: ", size=15))

    if app_state.EditorPage.info_mode == 'audio':
        info_page.append(ft.ElevatedButton('Добавить аудиодорожку'))
        info_page.append(ft.Divider(height=1))

    elif app_state.EditorPage.info_mode == 'subtitle':
        info_page.append(ft.ElevatedButton('Добавить субтитры'))
        info_page.append(ft.Divider(height=1))

    

    for index, state in enumerate(app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_file][app_state.EditorPage.info_mode]):
        if app_state.EditorPage.info_mode == 'audio':
            textField = audioChannel(state, index)

        elif app_state.EditorPage.info_mode == 'video':
            textField = videoChannel(state)
        
        elif app_state.EditorPage.info_mode == 'subtitle':
            textField = subtitleChannel(state, index)
                

        info_page.append(textField)


    return ft.Container(
        content=ft.Column(info_page)
    )





def navigation():
    return ft.Row(  # Лучше адаптируется для мобильных устройств
        controls=[
            ft.ElevatedButton(
                "Главная",
                on_click=lambda e: app_state.new_page(rout.multipage(1)),
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
        content=ft.Text("ABR Maker", size=30, weight='bold'),
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









     









