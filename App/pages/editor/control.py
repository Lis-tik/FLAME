
import flet as ft
from App.storage import app_state
import App.router as rout
from tkinter import Tk, filedialog
import os
from App.src.projectsControl.DataControl import add_track


class ConvertProfileDrop(ft.Dropdown):
    def __init__(self):
        super().__init__()
        self.value = None
        self.options = []
        self.on_change = self.changeProf

        for lang in app_state.LANGUAGE_LIST:
            self.options.append(ft.dropdown.Option(lang))


class LangDrop(ft.Dropdown):
    def __init__(self, lang):
        super().__init__()
        self.value = lang
        self.Label = "Выберите язык"
        self.hint_text = "Не выбрано!"
        self.on_change = self.changeLang
        self.border_color = ft.Colors.BLUE if self.value in app_state.LANGUAGE_LIST else ft.Colors.RED
        self.options = []
        
        for lang in app_state.LANGUAGE_LIST:
            self.options.append(ft.dropdown.Option(lang))


    def changeLang(self, e):
        for media in app_state.EditorPage.viewed_files:
            app_state.EditorPage.mediainfo_copy[media][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid]['language'] = self.value

        app_state.new_page(rout.Editor)





class actTrack(ft.ElevatedButton):
    def __init__(self, _uid):
        self._uid = _uid
        super().__init__(expand=True)
        self.text = app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode][_uid]['title'] if app_state.EditorPage.info_mode != 'video' else 'video'
        self.on_click = self.tracknum

        self.content = ft.Column(
            controls=[
                ft.Text(self.text, size=15),
                ft.Text(_uid, size=10, color=ft.Colors.GREY),
            ],
            spacing=0,
            tight=True
        )


        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if self._uid == app_state.EditorPage.viewed_uid else ft.Colors.WHITE),
        )

    def tracknum(self, e):
        app_state.EditorPage.viewed_uid = self._uid
        app_state.new_page(rout.Editor)




class addTrack(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.text = self.messageMode()
        self.on_click = self.open_directory_dialog


    def messageMode(self):
        if app_state.EditorPage.unification_mode:
            if app_state.EditorPage.info_mode == 'audio':
                return 'Добавить файл с аудиодорожками'
            elif app_state.EditorPage.info_mode == 'subtitle':
                return 'Добавить файл с субтитрами'
            elif app_state.EditorPage.info_mode == 'video':
                return 'Добавить файл с общими контейнерами'     
        else:
            if app_state.EditorPage.info_mode == 'audio':
                return 'Добавить аудиодорожку'
            elif app_state.EditorPage.info_mode == 'subtitle':
                return 'Добавить субтитры'
            elif app_state.EditorPage.info_mode == 'video':
                return 'Добавить видеодорожку'



    def open_directory_dialog(self, e):
        root = Tk()
        root.withdraw()  # Скрываем основное окно
        root.attributes('-topmost', True)  # Поверх других окон
        
        # Открываем диалог выбора директории
        list_cop = []

        if app_state.EditorPage.unification_mode:
            path = filedialog.askdirectory(title="Выберите папку")
            for meta in os.listdir(path):
                list_cop.append(f'{path}/{meta}')
        else:
            path = filedialog.askopenfilename(title="Выберите файл")
            list_cop.append(path)


        if list_cop:  # Если папка выбрана
            add_track(list_cop)

        app_state.new_page(rout.Editor)
            



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

        if not app_state.EditorPage.unification_mode:
            app_state.EditorPage.viewed_files.clear()
        else:
            app_state.EditorPage.viewed_files.clear()
            for edit in app_state.EditorPage.mediainfo_copy:
                app_state.EditorPage.viewed_files.append(edit)

        app_state.new_page(rout.Editor)


class RuleButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.on_click = self.modeFunc

        self.viewed = True if self.text in app_state.EditorPage.viewed_files else False

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=1),
            bgcolor=(ft.Colors.GREY_300 if self.viewed else ft.Colors.WHITE)
            )
    
    def modeFunc(self, e):
        if app_state.EditorPage.unification_mode:
            if not (self.text in app_state.EditorPage.viewed_files):
                app_state.EditorPage.viewed_files.append(self.text)
            else:
                app_state.EditorPage.viewed_files.remove(self.text)
        else:
            app_state.EditorPage.viewed_files = [self.text]
            
        app_state.new_page(rout.Editor)

    
        


class EditingInput(ft.TextField):
    def __init__(self):
        super().__init__()
        self.state = app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid]
        self.value = self.state['title']
        self.border_color = ft.Colors.BLUE if self.value else ft.Colors.RED
        self.hint_text = 'Поле должно быть заполнено!'
        self.on_change = self.handle_change

    
    def handle_change(self, e):
        for edit in app_state.EditorPage.viewed_files:
            app_state.EditorPage.mediainfo_copy[edit][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid]['title'] = self.value
        
        if not self.value:
            self.border_color = ft.Colors.RED
        else:
            self.border_color = ft.Colors.BLUE
        self.update()


class SampleMode(ft.Checkbox):
    def __init__(self):
        super().__init__()
        # self.on_change = self.SampleModeFunc

        self.value = False #if (len(app_state.mediainfo_Copy) == len(app_state.files)) else False

    def SampleModeFunc(self, e):
        for qulT in app_state.files:
            if not (len(app_state.activeFilesHome) == len(app_state.files)):
                app_state.activeFilesHome.append(qulT) 
                continue
            app_state.activeFilesHome.clear() 
            break

        app_state.new_page(rout.Editor)


class StatusCheck(ft.Checkbox):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.on_change = self.SampleModeFunc
        self.value = bool(app_state.EditorPage.mediainfo_copy[self.file]['status']) 

    def SampleModeFunc(self, e):
        app_state.EditorPage.mediainfo_copy[self.file]['status'] = int(not(app_state.EditorPage.mediainfo_copy[self.file]['status']))
        app_state.new_page(rout.Editor)

        

class StatusMediaFlag(ft.Checkbox):
    def __init__(self, _uid):
        super().__init__()
        self._uid = _uid
        self.on_change = self.dataCheck
        self.value = bool(int(app_state.EditorPage.mediainfo_copy[app_state.EditorPage.viewed_files[-1]][app_state.EditorPage.info_mode][self._uid]['status']))

    def dataCheck(self, e):
        for edit in app_state.EditorPage.viewed_files:
            app_state.EditorPage.mediainfo_copy[edit][app_state.EditorPage.info_mode][self._uid]['status'] = not(bool(app_state.EditorPage.mediainfo_copy[edit][app_state.EditorPage.info_mode][self._uid]['status']))
        app_state.new_page(rout.Editor)

        
     

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
        app_state.new_page(rout.Editor)


