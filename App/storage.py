


class ConvertConstructor:
    def __init__(self):
        self.audio = None
        self.video = None
        self.subtitle = None
        self.quality = None

class EditorPage:
    def __init__(self):
        self.info_mode = 'video'
        self.mediainfo_copy = None
        self.viewed_files = []
        self.viewed_track = None

        self.unification_mode = False
        
        self.debug = None
        self.DEBUG_COLORS = []


class AppState:
    def __init__(self):
        #Общие данные
        self.projects = None
        
        self.files  = []
        self.page = None

        self.global_path = None
        self.transition = False
        self.project_name = "Мой проект"
        self.AUDIO_FORMATS = ['.mkv', '.mka', 'mp4']
        self.SUBTITLES_FORMATS  = ['.srt', '.ass', '.vtt', '.sub', '.ttml', '.pgs']
        self.LANGUAGE_LIST = ['jpn', 'eng', 'rus']

        self.InfoData = None
        self._mediainfo_Original = None

        #HOME PAGE
        self.EditorPage = EditorPage()



    def new_page(self, new_page):
        print(f"Переход на новую страницу: {self.transition} -> {new_page}")
        self.page = new_page
        self.transition = True



    @property
    def mediainfo_Original(self):
        return self._mediainfo_Original

    @mediainfo_Original.setter
    def mediainfo_Original(self, new_value):
        self._mediainfo_Original = new_value
        self.EditorPage.mediainfo_copy = self.mediainfo_Original
        print(self.EditorPage.mediainfo_copy)
        
    
        
app_state = AppState()  # Глобальный экземпляр
