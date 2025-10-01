

class EditorPage:
    def __init__(self):
        self.info_mode = 'general'
        self.global_path = None
        self.mediainfo = None
        self.files  = []

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
        self.AUDIO_FORMATS = ['.mkv', '.mka', 'mp4']
        self.SUBTITLES_FORMATS  = ['.srt', '.ass', '.vtt', '.sub', '.ttml', '.pgs']
        self.LANGUAGE_LIST = ['jpn', 'eng', 'rus']

        self.CONVERT_PROFILES = []

        self.InfoData = None
        self.EditorPage = EditorPage()


    def new_page(self, new_page):
        print(f"Переход на новую страницу: {self.transition} -> {new_page}")
        self.page = new_page
        self.transition = True



        
    
        
app_state = AppState()  # Глобальный экземпляр


