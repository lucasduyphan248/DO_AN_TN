#import the necessary packages
import imutils
from imutils.video import VideoStream
import face_recognition
import cv2
import time
import os
import pickle
from collections import Counter
import sys
import subprocess

# Nhận tham số từ dòng lệnh
if len(sys.argv) != 2:
    print("Usage: python3 face_recog_camera.py <name>")
    sys.exit(1)

target_name = sys.argv[1]
print(f"Target name for recognition: {target_name}")

# dieu khien GPIO
gpio_available = True

dir_path = os.path.dirname(os.path.realpath(__file__))

print('[INFO] creating facial embeddings...', dir_path)
try:
    data = pickle.loads(open(os.path.join(dir_path, 'encodings.pickle'), 'rb').read())  # encodings here
except FileNotFoundError:
    print('Please train first')
    exit()

# turn on webcam
args = {}
args['display'] = 0  # Tắt hiển thị ảnh lên cửa sổ
args['detection_method'] = 'hog'

print('Starting camera ...')
vs = VideoStream(src=0).start()  # camera id = 0
time.sleep(2.0)

# lap camera
while True:
    frame = vs.read()  # doc tung anh trong camera
    if frame is None:
        print("Error: Could not read frame.")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)  # chuan hoa
    r = frame.shape[1] / float(rgb.shape[1])  # ti le

    # thuat toan phat hien khuon mat
    boxes = face_recognition.face_locations(rgb, model=args['detection_method'])
    encodings = face_recognition.face_encodings(rgb, boxes)

    names = []
    for encoding in encodings:
        votes = face_recognition.compare_faces(data['encodings'], encoding, tolerance=0.4)
        if True in votes:
            name = Counter([name for name, vote in list(zip(data['names'], votes)) if vote == True]).most_common()[0][0]
            if name == target_name:
                names.append(name)
            else:
                names.append('Unknown')
        else:
            names.append('Unknown')

    # Xóa đoạn vẽ khung bao quanh khuôn mặt
    for name in names:
        print("Name: ", name)
        #set GPIO17 high if the target face is recognized
        if gpio_available:
            if name == target_name:
                subprocess.run(["gpioset", "gpiochip0", "17=1"])
                print("relay_da_bat")
            else:
                print("relay_khong_bat")
        else:
            print("GPIO not available")
        #---------------------------------------------
    # if args['display'] == 1:
    #     cv2.imshow('Webcam', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

# close tat ca cua so
vs.stop()
cv2.destroyAllWindows()