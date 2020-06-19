# Face-detection-and-identification
Face identification

Requirements:
opencv-python
dlib
face-recognition
ecapture
numpy

Usage:
1. Put photo's in "dataset"
2. Run: python train.py --dataset dataset --encodings encodings.pickle
3.1. After that run: python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel (optional: cnn or hog. default is hog. CNN is more accurate but HoG is faster.)
Make sure your webcam is connected correctly. Sometimes it just doesn't see the webcam.
3.2. Now the program will check if there is a person. If there is it will start the blink detection to check if the person lives. After that it will look up who it is.