import os

import numpy as np
from scipy.io.wavfile import write

from better_profanity import profanity

import wave
import contextlib

import moviepy.editor
from pydub import AudioSegment

def video_to_audio(filepath):
    fileName = filepath + '.mp4'
    video = moviepy.editor.VideoFileClip(fileName)
    audio = video.audio
    audio.write_audiofile(filepath + ".mp3")

def wav_to_mp3(filepath):
    fileName = filepath + '.wav'
    AudioSegment.from_wav(fileName).export(filepath + '.mp3', format="mp3")
    # os.remove(filepath+'.wav')

def mp3_to_wav(filepath):
    fileName = filepath + '.mp3'
    AudioSegment.from_mp3(fileName).export(filepath + '.wav', format="wav")

def audio_analyse_fun(filename):

    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0+'\\video and audio data\\'
    # filename = '2'
    file = file_path +filename

    N_C_W_index = []
    # not common word index

    first_time_hr = []
    first_time_min = []
    first_time_sec = []
    first_time_millisec = []

    second_time_hr = []
    second_time_min = []
    second_time_sec = []
    second_time_millisec = []

    time_difference = []

    '''video to audio'''
    try:
        video_to_audio(file)
        mp3_to_wav(file)
    except:
        pass

    '''reading srt file and analysing with profanity filter'''

    with open(file_path + filename+'.srt', "r") as myFile:
        filter_string = myFile.read()
    filtered_string = profanity.censor(filter_string)
    # print(filtered)

    f = open(file_path + filename+".1.srt", "w+")
    f.write(filtered_string)
    f.close()

    '''converting text file to array of new and old srt file'''

    fileObj = open(file_path + filename+'.srt', "r")
    old_srt_array = fileObj.read().splitlines()
    fileObj.close()
    print(old_srt_array)

    fileObj1 = open(file_path + filename+'.1.srt', "r")
    new_srt_array = fileObj1.read().splitlines()
    fileObj1.close()
    print(new_srt_array)
    # print(new_srt_array[10][-1:])

    '''comparing both the arrays'''

    for a in range(0, len(old_srt_array)):
        if new_srt_array[a] == old_srt_array[a]:
            pass
        else:
            try:
                int(old_srt_array[a - 1][-1:])
                N_C_W_index.append(old_srt_array[a - 1])
                # print(N_C_W_index)
            except:
                N_C_W_index.append(old_srt_array[a - 2])

    # print(N_C_W_index)
    # print(old_srt_array[24])
    # print(len(old_srt_array[24]))

    '''time difference'''

    for b in range(0, len(N_C_W_index)):
        # print(N_C_W_index[b][0:2])
        first_time_hr.append(int(N_C_W_index[b][0:2]))
        first_time_min.append(int(N_C_W_index[b][3:5]))
        first_time_sec.append(int(N_C_W_index[b][6:8]))
        first_time_millisec.append(int(N_C_W_index[b][9:12]))

        second_time_hr.append(int(N_C_W_index[b][17:19]))
        second_time_min.append(int(N_C_W_index[b][20:22]))
        second_time_sec.append(int(N_C_W_index[b][23:25]))
        second_time_millisec.append(int(N_C_W_index[b][26:]))

        difference = ((second_time_hr[b] * 3600000) + (second_time_min[b] * 60000) + (second_time_sec[b] * 1000) +
                      second_time_millisec[b]) - \
                     ((first_time_hr[b] * 3600000) + (first_time_min[b] * 60000) + (first_time_sec[b] * 1000) +
                      first_time_millisec[b])
        time_difference.append(difference)

    # print(time_difference)

    '''beep sound generator'''

    for c in range(0, len(N_C_W_index)):
        sps = 44100
        freq_hz = 987.77
        duration = time_difference[c] / 1000
        vol = 1

        esm = np.arange(duration * sps)
        wf = np.sin(2 * np.pi * esm * freq_hz / sps)
        wf_quiet = wf * vol
        wf_int = np.int16(wf_quiet * 32767)
        write(file_path + "audio2.wav", sps, wf_int)

    '''audio file trimming'''

    fname = file_path + filename+'.wav'
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        # print(duration)

    # for d in range(0,len(N_C_W_index)):
    t1 = 0  # Works in milliseconds
    t2 = (first_time_hr[0] * 3600000) + (first_time_min[0] * 60000) + (first_time_sec[0] * 1000) + first_time_millisec[
        0]
    newAudio = AudioSegment.from_wav(file_path + filename+".wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(file_path + 'audio1.wav', format="wav")

    t1 = ((second_time_hr[0] * 3600000) + (second_time_min[0] * 60000) + (second_time_sec[0] * 1000) +
          second_time_millisec[0])  # Works in milliseconds
    t2 = duration * 1000
    newAudio = AudioSegment.from_wav(file_path + filename+".wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(file_path + 'audio3.wav', format="wav")

    '''audio files joining'''

    infiles = [file_path + "audio1.wav", file_path + "audio2.wav", file_path + "audio3.wav"]
    outfile = 'C:\\Harshith\\python projects\\hackbites2.0\\video and audio data\\' + "\\audio.wav"

    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

    '''removing unwanted files'''
    os.remove(file + '.1.srt')
    os.remove(file + '.mp3')
    os.remove(file + '.wav')
    os.remove(file_path + 'audio1.wav')
    os.remove(file_path + 'audio2.wav')
    os.remove(file_path + 'audio3.wav')
    # os.remove("C:\\Users\\harsh\\Downloads" + '\\format.txt')

    f1 = open(file_path0 + '\\front-end\\load.txt' + "", "w+")
    f1.write('success')
    f1.close()
