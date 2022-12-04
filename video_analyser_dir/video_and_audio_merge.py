from moviepy.editor import *

def merger(filepath):

    clip = VideoFileClip(filepath + '\\2.mp4')

    audioclip = AudioFileClip(filepath + "\\audio.wav")

    videoclip = clip.set_audio(audioclip)

    videoclip.write_videofile(filepath+'\\result.mp4')

