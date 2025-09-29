import json
import os
from pathlib import Path
from App.storage import app_state


def initialization_profiles():
    Path(f"./UserData/projects").mkdir(parents=True, exist_ok=True)

    profiles_list = [f for f in os.listdir('./UserData/ffmpegProfiles')]
    for profile in profiles_list:
        with open(f'./UserData/ffmpegProfiles/{profile}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            app_state.CONVERT_PROFILES.append(data)
            print(app_state.CONVERT_PROFILES)


def editProfiles():
    return

def changeSave():
    return 