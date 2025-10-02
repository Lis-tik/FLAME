

class ConverterProfile:
    def __init__(self):
        self.type = None


class EditorPage:
    def __init__(self):
        self.info_mode = 'general'
        self.global_path = None
        self.mediainfo = None
        self.files  = []

        self.fixation = None

        self.viewed_files = []
        self.viewed_track = None
        self.viewed_uid = None
        self.unification_mode = False
        
        self.debug_data = None
        self.DEBUG_COLORS = []


    @property
    def info_mode(self):
        return self._info_mode

    @info_mode.setter
    def info_mode(self, new_value):
        self._info_mode = new_value
        self.viewed_uid = None




class AppState:
    def __init__(self):
        self.projects = None
        self.page_control = None

        self.viewed_project = None
        self.page = None

        self.transition = False
        self.project_name = "Мой проект"
        self.MEDIA_FORMATS = [
            # Видео контейнеры
            '.mkv', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v',
            '.mpg', '.mpeg', '.m2ts', '.ts', '.mts', '.vob', '.ogv', '.3gp',
            
            # Аудио форматы
            '.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac', '.ogg', '.oga',
            '.opus', '.mka', '.ac3', '.dts', '.aiff', '.ape', '.wv', '.tta',
            
            # Специализированные видео форматы
            '.rm', '.rmvb', '.asf', '.divx', '.mxf', '.nut', '.yuv',
            
            # Изображения (только для кодирования/декодирования)
            '.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.avif',
            
            # Плейлисты и списки
            '.m3u', '.m3u8', '.pls',
            
            # Субтитры
            '.srt', '.ass', '.ssa', '.sub', '.vtt'
        ]
        self.LANGUAGE_LIST = ['jpn', 'eng', 'rus']

        self.CONVERT_PROFILES = []

        self.InfoData = None
        self.EditorPage = EditorPage()


    def new_page(self, new_page):
        print(f"Переход на новую страницу: {self.transition} -> {new_page}")
        self.page = new_page
        self.transition = True



        
    
        
app_state = AppState()  # Глобальный экземпляр


