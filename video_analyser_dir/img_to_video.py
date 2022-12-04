import os
from os.path import isfile, join
import cv2
import numpy as np

def fps_fun():
    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path+'2'

    cap= cv2.VideoCapture(filename+'.mp4')

    framespersecond= int(cap.get(cv2.CAP_PROP_FPS))

    return framespersecond

# print("The total number of frames in this video is ", framespersecond)

def convert_frames_to_video():
    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path + '2'
    pathOut = file_path+'stitched_video.mp4'

    fps = fps_fun()
    frame_array = []
    files = [f for f in os.listdir(file_path+'\\data') if isfile(join(file_path+'\\data', f))]

    # #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))

    for i in range(len(files)):
        filename=file_path+'\\data\\' + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = np.shape(img)
        size = (width,height)
        # print(filename)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

    for i in os.listdir(file_path+'\\data'):
        os.remove(file_path+'\\data\\'+i)
