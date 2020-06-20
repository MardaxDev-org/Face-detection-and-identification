# to start run: python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel
print("now!!!")
# remove mp3 to avoid errors
import os
os.remove("pad.mp3")
os.remove("niatfd.mp3")
# import the necessary packages
import cv2
import argparse
import time
import imutils
import numpy as np
import blinkcheck
import Voice as v
from imutils.video import VideoStream
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
                help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
                help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

go = 0

# initialize the video stream and allow the camera sensor to warmup
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while go == 0:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels

    # IMPORTANT: Sometimes an error can occur here. jusr rerun the command and most of the time it will work.
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    # grab the frame dimensions and convert it to a blob
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    (h, w) = frame.shape[:2]
    # pass the blob through the network and obtain the detections and predictions
    net.setInput(blob)
    detections = net.forward()
    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]
        # filter out weak detections by ensuring the `confidence` is greater than the minimum confidence
        if confidence < args["confidence"]:
            continue

        # compute the (x, y)-coordinates of the bounding box for the object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        # If it sees the face and it's close enough
        if confidence >= 0.90 and startX + startY + endX + endY <= 2000:
            print("Face in sight!!!")
            v.speak("Person at door", "en", "pad.mp3")
            time.sleep(0.5)
            if confidence >= 0.90:
                # start blinkcheck.py
                blinkcheck.cb()

        # draw the bounding box of the face along with the associated probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        cv2.putText(frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    # show the output frame
    cv2.imshow("Detectface", frame)
    key = cv2.waitKey(1) & 0xFF

    # if q is pressed, break from the loop
    if key == ord("q"):
        break

# cleanup
cv2.destroyAllWindows()
vs.stop()


