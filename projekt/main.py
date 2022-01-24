import argparse
import imutils
import cv2
import numpy as np

arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-i", "--image", default=None,
                       help="path to Image File ")
arg_parse.add_argument("-p", "--prototxt",
                       help="path to Caffe 'deploy' prototxt file",
                       default="MobileNetSSD_deploy.prototxt.txt")
arg_parse.add_argument("-m", "--model",
                       help="path to Caffe pre-trained model",
                       default="MobileNetSSD_deploy.caffemodel")
arg_parse.add_argument("-c", "--confidence", type=float, default=0.2,
                       help="minimum probability to filter weak detections")
args = vars(arg_parse.parse_args())

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

image = cv2.imread(args["image"])

# Resizing the Image
image = imutils.resize(image, width=min(400, image.shape[1]))

(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,
                             (300, 300), 127.5)

net.setInput(blob)
detections = net.forward()
people = 1
for i in np.arange(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with
    # the prediction
    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence > args["confidence"]:
        # extract the index of the class label from the
        # `detections`, then compute the (x, y)-coordinates of
        # the bounding box for the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        if CLASSES[idx] == "person":
            # draw the prediction on the frame
            label = "{}: {:.2f}%".format(CLASSES[idx],
                                         confidence * 100)
            print(label)
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
            people += 1

# show the output frame
print(f'Total Persons : {people - 1}')
cv2.imshow("Image", image)
cv2.waitKey(0)
