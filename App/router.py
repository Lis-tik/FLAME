
from App.pages.open.open import projects_manage
from App.pages.editor.editor_page import get_editor_page
from App.pages.multi_page import get_page_content
from App.pages.monitoring.monitoring import monitoring
from App.pages.navigation.navigation import navigation
from App.pages.introductory.introductory import introductory
from App.pages.settings.settings import settings
from App.pages.converter.converter import converter



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


Introductory = Router(0, introductory, 'Главная')
Navigation = Router(1, navigation, 'Навигация')
Projects = Router(2, projects_manage, 'Менеджер проектов')
Editor = Router(3, get_editor_page, 'Редактор проектов')
Monitoring = Router(4, monitoring, 'Мониторинг преобразования')
Converter = Router(5, converter, 'Конвертер')
Settings = Router(6, settings, 'Настройки')


