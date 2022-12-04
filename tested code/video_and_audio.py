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

