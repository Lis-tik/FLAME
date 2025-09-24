from App.storage import app_state
import json
from pathlib import Path
from datetime import datetime

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
