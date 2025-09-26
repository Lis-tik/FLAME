import ffmpeg
from App.src.Metadata_Receiving import video_info, audio_info, subtitle_info
from App.storage import app_state

def debug_info(instance):
    debug_messages = ''

    for file in instance:
        observed_list = {}
        for audio in instance[file]['audio']:
            if not audio['title']:
                debug_messages += (f'Аудиодорожка [{audio['index']}] не имеет описания\n')
            else:
                observed_list.setdefault(audio['title'], []).append(audio['index'])
                if len(observed_list[audio['title']]) > 1:
                    debug_messages += (f'Аудиодорожки [{observed_list[audio['title']]}] имеют одинаковое описание!')

    return debug_messages
            




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



def update_chanel(new_data):
    for index, value in enumerate(app_state.EditorPage.viewed_files):
        probe = ffmpeg.probe(new_data[index])

        for stream in probe['streams']:
            if stream['codec_type'] == 'audio':
                new_audio_chanel = audio_info(stream, new_data[index])
                app_state.EditorPage.mediainfo_copy[value]['audio'].append(new_audio_chanel)

            if stream['codec_type'] == 'subtitle':
                new_subtitle_chanel = subtitle_info(stream, new_data[index])
                app_state.EditorPage.mediainfo_copy[value]['subtitle'].append(new_subtitle_chanel)



    # if len(os.listdir(aud_lt)) < len(self.main_data):
    #     print(f'Предупреждение! В директории {aud_lt} с аудио, файлов меньше, чем в основной директории!')



















        


    def summary_data(self):
        summary_message = f'Всего файлов: {len(self.info_main_lib)}\n'

        pass_role = self.info_main_lib
        for x in range(len(pass_role)):

            pth = pass_role[x]

            summary_message += f'{x+1}.{pth['name']}: \n'

            summary_message += 'video: '
            for y in pth['video']:
                summary_message += f'{y['width']}x{y['height']}; pix_fmt: {y['pix_fmt']}'

            summary_message += '\naudio: \n'

            
            index = {}
            for z in range(len(pth['audio'])):
                cont = pth['audio'][z]

                if cont['path'] in index:
                    index[cont['path']] += 1
                else:
                    index[cont['path']] = 0

                cont['index'] = index[cont['path']]

                summary_message += f'--{z}. title: {cont['title']}; language: {cont['language']}; channel number: {cont['index']}; codec_name: {cont['codec_name']}; channels: {cont['channels']}; path: {cont['path']}\n'

            summary_message += 'subtitle: \n'
            for j in range(len(pth['subtitle'])):
                cont = pth['subtitle'][j]
                summary_message += f'--{j}. title: {cont['title']}; language: {cont['language']}; format: {cont['format']}; path: {cont['path']}\n'

            summary_message += '\n'
            
        return summary_message

                










