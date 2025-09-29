import ffmpeg
from App.src.projectsControl.Metadata_Receiving import video_info, audio_info, subtitle_info
from App.storage import app_state
import json
from pathlib import Path
from datetime import datetime


def start_getinfo():
    info_main_lib = {}
    for x in range(len(app_state.files)):
        name_path = app_state.files[x]

        info_main_lib[name_path] = { 
            'name': name_path,
            'path': app_state.global_path,
            'index': x+1,
            'status': 1,
            'video': {},
            'audio': {},
            'subtitle': {}
            }
    
        probe = ffmpeg.probe(f'{app_state.global_path}/{name_path}')
        for stream in probe['streams']:

            if stream['codec_type'] == 'video':
                video_data_add = video_info(stream)
                if video_data_add['uid'] in info_main_lib[name_path]['video']:
                    return
                info_main_lib[name_path]['video'][video_data_add['uid']] = video_data_add['data']
                    

            if stream['codec_type'] == 'audio':
                audio_data_add = audio_info(stream)
                if audio_data_add['uid'] in info_main_lib[name_path]['audio']:
                    return
                info_main_lib[name_path]['audio'][audio_data_add['uid']] = audio_data_add['data']

            if stream['codec_type'] == 'subtitle':
                subtitle_data_add = subtitle_info(stream)
                if subtitle_data_add['uid'] in info_main_lib[name_path]['subtitle']:
                    return
                
                info_main_lib[name_path]['subtitle'][subtitle_data_add['uid']] = subtitle_data_add['data']

    app_state.mediainfo_Original = info_main_lib



def add_track(new_data):
    for index, value in enumerate(app_state.EditorPage.viewed_files):
        probe = ffmpeg.probe(new_data[index])

        for stream in probe['streams']:
            if stream['codec_type'] == 'audio':
                new_audio_chanel = audio_info(stream, new_data[index])
                app_state.EditorPage.mediainfo_copy[value]['audio'][new_audio_chanel['uid']] = new_audio_chanel['data']

            if stream['codec_type'] == 'subtitle':
                new_subtitle_chanel = subtitle_info(stream, new_data[index])
                app_state.EditorPage.mediainfo_copy[value]['subtitle'][new_subtitle_chanel['uid']] = new_subtitle_chanel['data']



    # if len(os.listdir(aud_lt)) < len(self.main_data):
    #     print(f'Предупреждение! В директории {aud_lt} с аудио, файлов меньше, чем в основной директории!')



def saveChange():
    if not app_state.EditorPage.mediainfo_copy:
        return
    
    contentLibs = []
    for cont in app_state.EditorPage.mediainfo_copy:
        contentLibs.append(app_state.EditorPage.mediainfo_copy[cont])

    data = {
        "name": app_state.project_name,
        "changeData": str(datetime.now()),
        "content": contentLibs
    }


    file_path = Path(f"./UserData/projects/{app_state.project_name}/data.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)