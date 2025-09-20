
from App.pages.open.open import projects_manage
from App.pages.editor.editor_page import get_editor_page
from App.pages.multi_page import get_page_content
from App.pages.Setting_converter import setting_converter
from App.pages.navigation.navigation import navigation
from App.pages.main.main import main



def multipage(data):
    return Router(3, get_page_content, 'Страница', data)


class Router:
    def __init__(self, page, link, title, data=None):
        self.page = page
        self.link = link
        self.title = title
        self.data = data

    def routdata(self, data):
        self.data = data


Main = Router(0, main, 'Главная')
Navigation = Router(1, navigation, 'Навигация')
Projects = Router(2, projects_manage, 'Создайте проект!')
Editor = Router(3, get_editor_page, 'Домашняя страница')
Page_setting_converter = Router(4, setting_converter, 'Настройки конвертера')

