from mtcnn import MTCNN
import cv2
import json

img2 = input("Image: ")
#img2 = 'unnamed.jpg'
img = cv2.cvtColor(cv2.imread(img2), cv2.COLOR_BGR2RGB)
detector = MTCNN()
data = detector.detect_faces(img)

bounding_box = data
point = bounding_box[0]["keypoints"]
img3 = img2.split(".")
name = img3[0] + ".txt"
output = open(name, "a")
for key in point:
    points = list(point[key])
    print(str(points[0]) + " " + str(points[1]), file=output)
output.close()
