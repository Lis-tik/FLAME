import ffmpeg
import os
from src.Metadata_Receiving import video_info, audio_info, subtitle_info

class Info():
    def __init__(self):
        self.container = []
        self.info_main_lib = []
        self.conteg = {}
        self.global_path = ''

    def debug_info(self, instance):
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
                



    def edit_workspace(self):
        print('Вы в режиме редактирования\nНажмите [ENTER] для выхода')
        mode = int(input('Выберете номер медиа, которое хотите редактировать\nВведите (-1), чтобы выбрать ВСЕ медия\n:'))
        correct = input('Внесите корректировки\n\nФормат: тип данных в медиа/номер дорожки/параметр/новое значение\nПример: audio/0/title/new_name\n:').split('/')

        if mode == -1:
            for x in range(len(self.info_main_lib[self.global_path])):
                if correct[2]:
                    self.info_main_lib[x][correct[0]][int(correct[1])][correct[2]] = correct[3]
                else:
                    del self.info_main_lib[x][correct[0]][int(correct[1])]
        else:
            self.info_main_lib[mode][correct[0]][int(correct[1])][correct[2]] = correct[3]


    


    def start_getinfo(self, container, global_path):
        self.container = container
        self.global_path = global_path

        self.info_main_lib = {}
        for x in range(len(self.container)):
            name_path = self.container[x]

            self.info_main_lib[name_path] = { 
                'name': name_path,
                'path': global_path,
                'index': x+1,
                'status': 1,
                'video': [],
                'audio': [],
                'subtitle': []
                }
            

        
            probe = ffmpeg.probe(f'{global_path}/{name_path}')
            for stream in probe['streams']:

                if stream['codec_type'] == 'video':
                    video_data_add = video_info(stream)
                    self.info_main_lib[name_path]['video'].append(video_data_add)
                        

                if stream['codec_type'] == 'audio':
                    audio_data_add = audio_info(stream)
                    self.info_main_lib[name_path]['audio'].append(audio_data_add)

                if stream['codec_type'] == 'subtitle':
                    subtitle_data_add = subtitle_info(stream)
                    self.info_main_lib[name_path]['subtitle'].append(subtitle_data_add)

        
        return self.info_main_lib



    def update_chanel(self, new_data):
        for x in range(len(new_data)):
            probe = ffmpeg.probe(new_data[x])

            for stream in probe['streams']:
                if stream['codec_type'] == 'audio':

                    new_audio_chanel = self.audio_info(stream, new_data[x])
                    self.info_main_lib[x]['audio'].append(new_audio_chanel)

                if stream['codec_type'] == 'subtitle':
                    new_subtitle_chanel = self.subtitle_info(stream, new_data[x])
                    self.info_main_lib[x]['subtitle'].append(new_subtitle_chanel)


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

                










