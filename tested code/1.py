from audio_analyser_dir import video_and_audio
from audio_analyser_dir import profanity_filter
from audio_analyser_dir import comparing_arrays
from audio_analyser_dir import time_difference
from audio_analyser_dir import bleep_sound_generator

if __name__ == '__main__':

    '''file path'''

    path = 'C:\\Harshith\\python projects\\hackbites2.0\\video and audio data\\'
    file_path = path + '2'
    # print(file_path)

    '''video to audio conversion for further use'''

    video_and_audio.video_to_audio(file_path)
    video_and_audio.mp3_to_wav(file_path)

    '''Filtering the srt file text'''

    old_srt_array, new_srt_array = profanity_filter.profanity_class(file_path).filteration()
    # print(old_srt_array)

    '''comparing arrays'''
    # not common word index
    N_C_W_index = comparing_arrays.compare_array().compare()

    '''time_difference'''

    time_difference = time_difference.time_diff_class(N_C_W_index).difference()

    '''bleep sound generator'''

    bleep_sound_generator.bleep_sound_class(time_difference,N_C_W_index,file_path)

    '''audio file trimming'''



