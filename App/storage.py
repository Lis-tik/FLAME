
from src.media_info import Info



class EditorPage:
    def __init__(self):
        self.info_mode = 'video'
        self.mediainfo_copy = None
        self.viewed_files = []

        self.unification_mode = False
        
        self.debug = None
        self.DEBUG_COLORS = []




class AppState:
    def __init__(self):
        #Общие данные
        self._files  = []
        self.page = None

        self.global_path = None
        self.transition = False
        self.project_name = "Мой проект"
        self.AUDIO_FORMATS = ['.mkv', '.mka', 'mp4']
        self.SUBTITLES_FORMATS  = ['.srt', '.ass', '.vtt', '.sub', '.ttml', '.pgs']

        self.InfoData = Info()
        self.mediainfo_Original = None

        #HOME PAGE
        self.EditorPage = EditorPage()




    def new_page(self, new_page):
        print(f"Переход на новую страницу: {self.transition} -> {new_page}")
        self.page = new_page
        self.transition = True



    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, new_value):
        self._files = new_value

        self.mediainfo_Original = self.InfoData.start_getinfo(self._files, self.global_path)
        self.EditorPage.mediainfo_copy = self.mediainfo_Original

        # print(self.mediainfo_Original)
        
    
        
app_state = AppState()  # Глобальный экземпляр
