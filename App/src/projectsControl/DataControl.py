import ffmpeg
from App.src.projectsControl.Metadata_Receiving import video_info, audio_info, subtitle_info
from App.src.debugcontrol import debug_analysis
from App.storage import app_state
import json
from pathlib import Path
from datetime import datetime
import hashlib
import os

def start_getinfo():
    info_main_lib = {}
    for x in range(len(app_state.EditorPage.files)):
        name_path = app_state.EditorPage.files[x]
        probe = ffmpeg.probe(f'{app_state.EditorPage.global_path}/{name_path}')


        info_main_lib[name_path] = { 
            'name': name_path,
            'path': app_state.EditorPage.global_path,
            'duration': float(probe['format']['duration']),
            'index': x+1,
            'status': 1,
            'video': {},
            'audio': {},
            'subtitle': {}
            }
    
        for stream in probe['streams']:
            if stream['codec_type'] == 'video':
                video_data_add = video_info(stream)
                uid = hashlib.md5(str(video_data_add).encode()).hexdigest()
                info_main_lib[name_path]['video'][uid] = video_data_add
                    

            if stream['codec_type'] == 'audio':
                audio_data_add = audio_info(stream)
                uid = hashlib.md5(str(audio_data_add).encode()).hexdigest()
                info_main_lib[name_path]['audio'][uid] = audio_data_add

            if stream['codec_type'] == 'subtitle':
                subtitle_data_add = subtitle_info(stream)
                uid = hashlib.md5(str(subtitle_data_add).encode()).hexdigest()
                info_main_lib[name_path]['subtitle'][uid] = subtitle_data_add

    app_state.EditorPage.mediainfo = info_main_lib
    print(app_state.EditorPage.mediainfo)



def add_track(new_data):
    for index, value in enumerate(app_state.EditorPage.viewed_files):
        probe = ffmpeg.probe(new_data[index])

        for stream in probe['streams']:
            if stream['codec_type'] == 'audio':
                new_audio_chanel = audio_info(stream, new_data[index])
                uid = hashlib.md5(str(new_audio_chanel).encode()).hexdigest()
                app_state.EditorPage.mediainfo[value]['audio'][uid] = new_audio_chanel

            if stream['codec_type'] == 'subtitle':
                new_subtitle_chanel = subtitle_info(stream, new_data[index])
                uid = hashlib.md5(str(new_subtitle_chanel).encode()).hexdigest()
                app_state.EditorPage.mediainfo[value]['subtitle'][uid] = new_subtitle_chanel



def dataEdit(key, new_value):
    for media in app_state.EditorPage.viewed_files:
        if not app_state.EditorPage.viewed_uid in app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode]:
            print(f"Предупреждение! В файле {media} не обнаружена аудиодорожка с хешем [{app_state.EditorPage.viewed_uid}]")
            continue
        
        app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid][key] = new_value
    
        new_uid = app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode][app_state.EditorPage.viewed_uid]
        new_uid = hashlib.md5(str(new_uid).encode()).hexdigest()
        app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode][new_uid] = app_state.EditorPage.mediainfo[media][app_state.EditorPage.info_mode].pop(app_state.EditorPage.viewed_uid)

    debug_analysis()
    app_state.EditorPage.viewed_uid = new_uid


    # if len(os.listdir(aud_lt)) < len(self.main_data):
    #     print(f'Предупреждение! В директории {aud_lt} с аудио, файлов меньше, чем в основной директории!')


def unpackingData(proj):
    with open(f'./UserData/projects/{proj}/data.json', 'r', encoding='utf-8') as file:
        app_state.EditorPage.mediainfo = {}
        
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


    file_path = Path(f"./UserData/projects/{app_state.project_name}/data.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)