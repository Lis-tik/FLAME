from App.storage import app_state
import json
from pathlib import Path
from datetime import datetime
import os




def initialization_profiles():
    Path(f"./UserData/projects").mkdir(parents=True, exist_ok=True)

    profiles_list = [f for f in os.listdir('./UserData/ffmpegProfiles')]
    for profile in profiles_list:
        with open(f'./UserData/ffmpegProfiles/{profile}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            app_state.CONVERT_PROFILES




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
