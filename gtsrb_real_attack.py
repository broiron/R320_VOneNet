import os
import random
import cv2 as cv
import math

# root directory path for archive train data 
DataPath = "/Users/broiron/Desktop/archive/Train"
dir = os.listdir(DataPath)

# Line Color setting
white_color = (255, 255, 255)
black_color = (0, 0, 0)

color = [white_color, black_color]
# How many lines? -> 1 to 4
line = [1, 2, 3, 4]
# Drawing Lines
for i in dir:
    subdir = DataPath+"/"+i
    # Because of Mac file-system
    if i == ".DS_Store":
        continue
    datalist = os.listdir(subdir)
    print(subdir, len(datalist))
    # Access to image
    for j in datalist:
        image = j
        print(image)
        img = cv.imread(subdir+"/"+image)
        if img is None:
            continue
        h, w, c = img.shape
        # img2 = clahe(img)
        img2 = img
        # image resize (Bigger)
        img2 = cv.resize(img2, dsize=(90, 90), interpolation=cv.INTER_LINEAR_EXACT)
        # #of lines selecting, 1 to 4
        line_choice = random.choice(line)
        for k in range(line_choice):
            # To prevent long line, Check distance
            while True:
                x1 = random.randint(20, 60)
                y1 = random.randint(20, 60)
                x2 = random.randint(20, 60)
                y2 = random.randint(20, 60)
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance < 50:
                    break
            width = random.randint(1, 3)
            color_choice = random.choice(color)
            cv.line(img2, (x1, y1), (x2, y2), color_choice, width, cv.LINE_AA)
        img2 = cv.resize(img2, dsize=(w, h), interpolation=cv.INTER_AREA)
        path = '/Users/broiron/Desktop/AttackedData/' + i
        os.makedirs(path, exist_ok=True)
        # Store image
        if not (cv.imwrite("/Users/broiron/Desktop/AttackedData/" + i + "/" + image + ".png", img2)):
            exit(1)
