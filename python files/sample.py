import speech_recognition as sr

AUDIO_FILE=(C:/Harshith/python projects/hackbites2.0/video and audio data/audio.wav)
r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    # sr.recognize_api()
    googletext = r.recognize_google(audio)
    with open("audio5.txt","w") as f:
            f.write(googletext)
    with open("audio.srt","w") as f:
            f.write(googletext)