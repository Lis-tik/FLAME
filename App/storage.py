

class ConverterProfile:
    def __init__(self):
        self.type = None


class EditorPage:
    def __init__(self):
        self.info_mode = 'general'
        self.global_path = None
        self.mediainfo = {}
        self.files  = []

        self.bashPreview_mode = 0

        self.fixation = None

        self.viewed_files = []
        self.viewed_track = None
        self.viewed_uid = None
        self.unification_mode = False
        
        self.debug_data = None



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


        self.LANGUAGE_LIST = {
            'jpn': 'Японский',
            'eng': 'Английский', 
            'rus': 'Русский',

            'spa': 'Испанский', 'fra': 'Французский', 'deu': 'Немецкий', 'ita': 'Итальянский', 'por': 'Португальский', 'chi': 'Китайский',
            'kor': 'Корейский', 'ara': 'Арабский', 'hin': 'Хинди', 'tur': 'Турецкий', 'vie': 'Вьетнамский', 'tha': 'Тайский', 'nld': 'Нидерландский',
            'swe': 'Шведский', 'nor': 'Норвежский', 'dan': 'Датский', 'fin': 'Финский', 'pol': 'Польский', 'ukr': 'Украинский', 'bel': 'Белорусский',
            'ces': 'Чешский', 'slk': 'Словацкий', 'hun': 'Венгерский', 'ron': 'Румынский', 'bul': 'Болгарский', 'ell': 'Греческий', 'heb': 'Иврит',
            'fas': 'Персидский', 'urd': 'Урду', 'ben': 'Бенгальский', 'tam': 'Тамильский', 'mar': 'Маратхи', 'tel': 'Телугу', 'ind': 'Индонезийский',
            'msa': 'Малайский', 'fil': 'Филиппинский', 'swa': 'Суахили', 'zul': 'Зулу', 'afr': 'Африкаанс', 'cat': 'Каталанский', 'eusk': 'Баскский',
            'glg': 'Галисийский', 'isl': 'Исландский', 'lav': 'Латышский', 'lit': 'Литовский', 'est': 'Эстонский', 'mal': 'Малаялам', 'kan': 'Каннада',
            'pan': 'Панджаби', 'guj': 'Гуджарати', 'ori': 'Ория', 'mya': 'Бирманский', 'khm': 'Кхмерский', 'lao': 'Лаосский', 'sin': 'Сингальский',
            'nep': 'Непальский', 'mon': 'Монгольский','amh': 'Амхарский', 'hau': 'Хауса', 'yor': 'Йоруба', 'ibo': 'Игбо', 'sna': 'Шона',
            'som': 'Сомалийский', 'tgl': 'Тагальский'
        }


        self.CONVERT_PROFILES = {}
        self.viewed_profile = None

        self.InfoData = None
        self.EditorPage = None


    @property
    def viewed_project(self):
        return self._viewed_project

    @viewed_project.setter
    def viewed_project(self, new_value):
        self._viewed_project = new_value
        self.EditorPage = EditorPage()
        print("ПРОЕКТ СМЕНИЛСЯ")



    def new_page(self, new_page):
        print(f"Переход на новую страницу: {self.transition} -> {new_page}")
        self.page = new_page
        self.transition = True



        
    
        
app_state = AppState() 

