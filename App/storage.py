
from src.media_info import Info


class AppState:
    def __init__(self):
        self._files  = []
        self.page = None

        self.global_path = None
        self._transition = False
        self.project_name = "Мой проект"
        self.audio_formats = ['.mkv', '.mka', 'mp4']
        self.subtitles_formats = ['.srt', '.ass', '.vtt', '.sub', '.ttml', '.pgs']

        self.activeFilesHome = []
        self.infoMode = 'video'

        self.InfoData = Info()
        self.mediainfo_Original = None
        self.mediainfo_Copy = None

    def at_work_files(self):
        for media in self.mediainfo_Copy:
            return


    def new_page(self, new_page):
        self.page = new_page
        self.transition = True
    
    @property
    def falg_transition(self):
        return self._transition
    
    @falg_transition.setter
    def transition(self, new_value):
        print(f"Переход на новую страницу: {self._transition} -> {new_value}")
        self._transition = new_value



    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, new_value):
        self._files = new_value

        self.mediainfo_Original = self.InfoData.start_getinfo(self._files, self.global_path)
        self.mediainfo_Copy = self.mediainfo_Original

        print(self.mediainfo_Original)
        
    
        
app_state = AppState()  # Глобальный экземпляр
