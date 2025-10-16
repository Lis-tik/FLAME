import subprocess
import os
from App.storage import app_state
from pathlib import Path
from App.src.manifest.manifestCreator import MakerMPD



def command_creation(obj):
    cmd = ['ffmpeg']
    for key, value in obj.items():
        if key != 'output':
            cmd.append(key)
        if value:
            cmd.append(str(value))

    return(cmd)


def start():
    
    for media in app_state.EditorPage.mediainfo:
        media = app_state.EditorPage.mediainfo[media]
        
        if not media['status']:
            continue

        for mode in ['video', 'audio', 'subtitle']:
            for track in media[mode]:

                if not media[mode][track]['status']:
                    continue
                
                for profile in media[mode][track]['converted']:
                    Path(os.path.dirname(media[mode][track]['converted'][profile]['output'])).mkdir(parents=True, exist_ok=True)
                    cmd = command_creation(media[mode][track]['converted'][profile])

                    try:
                        subprocess.run(cmd, check=True, text=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Ошибка FFmpeg: {e.stderr}")

        debugStart = MakerMPD(global_path=media['output'])
        debugStart.main_control()




