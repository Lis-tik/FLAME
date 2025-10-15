import json
import os
from pathlib import Path
from App.storage import app_state




def transformation():
    for file in app_state.EditorPage.viewed_files:
        media = app_state.EditorPage.mediainfo[file]

        for mode in ['video', 'audio', 'subtitle']:
            for track in media[mode]:
                
                if app_state.CONVERT_PROFILES[media['profile']][mode]['quality']:
                    for quality in app_state.CONVERT_PROFILES[media['profile']][mode]['quality']:
                        if quality['height'] <= media[mode][track]['height']:

                            command = ['ffmpeg', 
                                       '-i', str(f'{media['path']}/{media['name']}'),
                                       '-vf', str({quality['vf']}),
                                       '-crf', str({quality['crf']})
                                       ]


                            for key in app_state.CONVERT_PROFILES[media['profile']][mode]['arguments']:
                                value = app_state.CONVERT_PROFILES[media['profile']][mode]['arguments'][key]
                                command.append(key)
                                command.append(value)


                            command.append(f'{quality['name']}')
                            if command not in media[mode][track]['converted']:
                                media[mode][track]['converted'].append(command)
                                
                else:
                    command = ['ffmpeg', 
                                '-i', str(f'{media['path']}/{media['name']}')
                                ]

                    for key in app_state.CONVERT_PROFILES[media['profile']][mode]['arguments']:
                        value = app_state.CONVERT_PROFILES[media['profile']][mode]['arguments'][key]
                        command.append(key)
                        command.append(value)

                    command.append(f'')

                    if command not in media[mode][track]['converted']:
                        media[mode][track]['converted'].append(command)




def editProfiles(key, new_value):
    return


def initialization_profiles():
    Path(f"./UserData/ffmpegProfiles").mkdir(parents=True, exist_ok=True)

    profiles_list = [f for f in os.listdir('./UserData/ffmpegProfiles')]
    for profile in profiles_list:
        with open(f'./UserData/ffmpegProfiles/{profile}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            app_state.CONVERT_PROFILES[data['profile']['name']] = data['profile']



def changeSave():
    return