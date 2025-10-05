import json
import os
from pathlib import Path
from App.storage import app_state


def initialization_profiles():
    app_state.CONVERT_PROFILES = []
    Path(f"./UserData/ffmpegProfiles").mkdir(parents=True, exist_ok=True)

    profiles_list = [f for f in os.listdir('./UserData/ffmpegProfiles')]
    for profile in profiles_list:
        with open(f'./UserData/ffmpegProfiles/{profile}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            app_state.CONVERT_PROFILES.append(data)


def editProfiles():
    return

def changeSave():
    return 