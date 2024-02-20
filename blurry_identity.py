import cv2
import pyvirtualcam
import random
import argparse

width, height = 640, 480

# You can change the following values in the program

fps = 60 # Change if quantity is low or you need
camera_index = 1 # Change if your camera has a different index
scale_factor = 1.2 # Change if you don't like the default sensitivity value
padding = 30 # Change if you want to increase or decrease the crystal window size
blur_value = (99,11) # Change if you want more or less crystal amount
frame_text = "blured face" # Change the default face text value
frame_title = 'Camera Preview' # Change the default value of the preview window

parser = argparse.ArgumentParser()
parser.add_argument("--preview", dest="preview",action="store_true",help="Show a preview windows with open-cv")
parser.add_argument("--dont-show-text", dest="show_text",action="store_true",help="Show text in frame")
parser.add_argument("--text", dest="frame_text",type=str,help="Customize text in frame")
args = parser.parse_args()

if args.frame_text:
    frame_text = args.frame_text

def random_blur_value(min_num, max_num):
    min_odd = min_num if min_num % 2 != 0 else min_num + 1
    max_odd = max_num if max_num % 2 != 0 else max_num - 1
    if min_odd > max_odd:
        return None  
    random_odd_1 = random.randint(min_odd, max_odd)
    random_odd_2 = random.randint(min_odd, max_odd)
    
    if random_odd_1 % 2 == 0:
        random_odd_1 += 1
    
    if random_odd_2 % 2 == 0:
        random_odd_2 += 1
    
    return (random_odd_1, random_odd_2)


def detect_and_blur_faces(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, scale_factor, 10)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            x, y, w, h = x - padding, y - padding, w + (padding * 2),h + (padding * 2)
            
            face_roi = frame[y:y+h, x:x+w]
            blurred_face = cv2.GaussianBlur(face_roi, random_blur_value(61,113), 0)
            frame[y:y+h, x:x+w] = blurred_face
            
            if not args.show_text:
                cv2.putText(
                    frame,
                    frame_text,
                    (x,y),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    0.7,
                    (0,255,0),
                    1,
                    cv2.LINE_4
                )

    else:
        frame = cv2.GaussianBlur(frame, random_blur_value(61,113), 0)

    return frame

def generate_frame():
    with pyvirtualcam.Camera(width=width, height=height, fps=fps, fmt=pyvirtualcam.PixelFormat.BGR) as cam:
        cap = cv2.VideoCapture(camera_index)
        print("Ctrl+C for Exit")

        while True:
            try:
                ret, frame = cap.read()

                if ret:
                    frame = detect_and_blur_faces(frame)
                    
                    if args.preview == True:
                        cv2.imshow(frame_title, frame)
                    cam.send(frame)

                cv2.waitKey(30)
            except KeyboardInterrupt:
                cam.close()
                cv2.destroyAllWindows()
try:    
    generate_frame()
except AttributeError:
    pass
