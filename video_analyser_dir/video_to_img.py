
import cv2
import os

def video_to_img_fun():

    file_path0 = 'C:\\Harshith\\python projects\\hackbites2.0'
    file_path = file_path0 + '\\video and audio data\\'
    filename = file_path+'2'
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

video_to_img_fun()