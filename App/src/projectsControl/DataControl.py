import ffmpeg
from App.src.projectsControl.intelligence import get_intelligence, videostream, audiostream, subtitles
from App.src.debugcontrol import debug_analysis
from App.storage import app_state, EditorPage
import json
from pathlib import Path
from datetime import datetime



def autopath(path):
    for media in app_state.EditorPage.viewed_files: 
        app_state.EditorPage.mediainfo[media]['output'] = f'{path}/{app_state.viewed_project}_[by.MUXON]'

        for mode in ['audio', 'video', 'subtitle']:
            for track in app_state.EditorPage.mediainfo[media][mode]:
                app_state.EditorPage.mediainfo[media][mode][track]['output'] = f'{path}/{app_state.viewed_project}_[by.MUXON]/{mode}/{'video' if mode == 'video' else app_state.EditorPage.mediainfo[media][mode][track]['title']}'


def start_getinfo(path):
    app_state.fixation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for x in range(len(app_state.EditorPage.files)):
        name_path = app_state.EditorPage.files[x]

        new_data = {
            'name': name_path,
            'path': path
        }

        get_intelligence(new_data)


def add_track(new_data):
    app_state.fixation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for index, value in enumerate(app_state.EditorPage.viewed_files):
        get_intelligence({"name": value}, new_data)


def add_file(name, path):
    get_intelligence({"name": name, "path": path})



def dataEdit(key, new_value):
    for media in app_state.EditorPage.viewed_files:
        if not (app_state.EditorPage.viewed_uid in app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode]):
            print(f"Предупреждение! В файле {media} не обнаружена аудиодорожка с uid [{app_state.EditorPage.viewed_uid}]")
            continue
            
        app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid][key] = new_value

    debug_analysis()



    # if len(os.listdir(aud_lt)) < len(self.main_data):
    #     print(f'Предупреждение! В директории {aud_lt} с аудио, файлов меньше, чем в основной директории!')


def unpackingData(proj):
    with open(f'./UserData/projects/{proj}/data.json', 'r', encoding='utf-8') as file:
        
        data = json.load(file)
        for media in data['content']:
            app_state.EditorPage.mediainfo[media['name']] = media


            
        



def saveChange():
    if not app_state.EditorPage.mediainfo:
        return
    
    contentLibs = []
    for cont in app_state.EditorPage.mediainfo:
        contentLibs.append(app_state.EditorPage.mediainfo[cont])

    data = {
        "name": app_state.project_name,
        "changeData": str(datetime.now()),
        "content": contentLibs
    }


    file_path = Path(f"./UserData/projects/{app_state.viewed_project}/data.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

