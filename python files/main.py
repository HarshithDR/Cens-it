from audio_analyser_dir import audio_analyse
from video_analyser_dir import video_analyse

import os

if __name__ == '__main__':
    file_path0 = os.getcwd()
    file_path = file_path0 + 'video and audio data'
    f_file_path = "C:\\Users\\harsh\\Downloads"
    while True:
        f = open(file_path0 + '\\front-end\\load.txt' + "", "w+")
        f.write('true')
        f.close()
        f = open(file_path0 + '\\front-end\\output.txt' + "", "w+")
        f.write('N/A')
        f.close()
        try:
            os.path.exists(f_file_path + '\\format.txt')

            with open(f_file_path + '\\format.txt') as f:
                type = f.read()
            f.close()
            filename = '2'

            if type == 'audio' or 'live':
                audio_analyse.audio_analyse_fun(filename)
                f2 = open(file_path0 + '\\front-end\\output.txt' + "", "w+")
                f2.write('U/A')
                f2.close()

            elif type == 'video':
                audio_analyse.audio_analyse_fun(filename)
                x = video_analyse.video_analyse_fun(filename)
                if x >100:
                    f3 = open(file_path0 + '\\front-end\\output.txt' + "", "w+")
                    f3.write('A')
                    f3.close()
            else:
                pass
            os.remove(f_file_path + '\\format.txt')

        except:
            pass