# # import video_and_audio_merge
# import img_to_video
# # from tensorflow.keras.models import load_model
# import numpy as np
# import video_to_img
# import os
from moviepy.editor import *
import os
from os.path import isfile, join
import cv2
import numpy as np
from tensorflow.keras.models import load_model


def video_to_img_fun(file):
    print('deframming video')
    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path+file
    cam = cv2.VideoCapture(filename+'.mp4')
    try:
        # creating a folder named data
        if not os.path.exists(file_path+'data'):
            os.makedirs(file_path+'data')

    # if not created then raise error
    except OSError:
        pass
    # frame
    currentframe = 0

    while True:
        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = file_path+'data\\' + str(currentframe) + '.jpg'

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

def fps_fun():
    print('calculating_fps')
    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path+'2'

    cap= cv2.VideoCapture(filename+'.mp4')

    framespersecond= int(cap.get(cv2.CAP_PROP_FPS))

    return framespersecond

# print("The total number of frames in this video is ", framespersecond)

def convert_frames_to_video(file):
    print('stitching video frames')
    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path + file
    pathOut = file_path+'stitched.mp4'

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


def merger(filepath,filename):
    print('merging audio with video')
    clip = VideoFileClip(filepath + '\\'+'stitched.mp4')

    audioclip = AudioFileClip(filepath + "\\audio.wav")

    videoclip = clip.set_audio(audioclip)

    videoclip.write_videofile(filepath+'\\results.mp4')
    return 0


def blank_img_fun(img_name):

    from PIL import Image as im
    img = cv2.imread(img_name)
    # img = np.zeros([100,100,3],dtype=np.uint8)
    # img.fill(0) # or img[:] = 255
    img1 = np.ones([240, 320, 3], dtype=np.uint8)

    # out =  np.concatenate((img, img1), axis = 0)
    out = np.multiply(img, img1)

    data = im.fromarray(out)
    data.save(img_name)

def video_analyse_fun(filename):
    print('starting')

    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0+'\\video and audio data\\'
    # filename
    file = file_path +filename

    '''output file writing'''

    f = open(file_path0+'\\front-end\\load.txt', "w+")
    f.write('true')
    f.close()

    '''video to image'''
    video_to_img_fun(filename)

    '''cnn model'''
    '''model integration and prediction'''
    classify_number = 0
    model = load_model('imgclassifier.h5')
    os.chdir("C:\\Harshith\\python projects\\hackbites2.0\\video and audio data\\data")
    files = os.listdir("C:\\Harshith\\python projects\\hackbites2.0\\video and audio data\\data")
    # os.chdir()
    for img in files:
        predict = model.predict(img)
        if predict == 'notnormal':
            '''blank'''
            blank_img_fun()
            classify_number+=1
        elif predict == 'violence':
            '''blank'''
            blank_img_fun()
            classify_number+=1

    '''image to video'''
    convert_frames_to_video(filename)


    '''video and audio merge'''

    merger(file_path,filename)
    f1 = open(file_path0 + '\\front-end\\load.txt' + "", "w+")
    f1.write('success')
    f1.close()
    os.remove(file_path + "\\audio.wav")
    os.remove(file_path + "\\stitched.mp4")
    return classify_number
    # exit()

    '''output file writing'''

    # f = open(file_path0+'\\front-end\\load.txt' + "", "w+")
    # f.write('success')
    # f.close()

# video_analyse_fun('2')

