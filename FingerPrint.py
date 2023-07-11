import cv2
import array
import numpy as np
import csv
import pandas as pd
import  math as m
import  statistics as st

im = cv2.imread('./Test/449__F_Left_little_finger.bmp', cv2.IMREAD_GRAYSCALE)
def imageMoments():
    moments = cv2.moments(im)
    huMoments = cv2.HuMoments(moments)
    cv2.imshow("Original Finger", im)
    cv2.waitKey(1)
    for i in range(0, 7):
        t = -1 * (m.copysign(1.0, huMoments[i]) * m.log10(abs(huMoments[i])))
        huMoments[i] = t
        print(huMoments[i])
    mean2 = np.mean(huMoments)
    print(mean2)
    return mean2

def compare(mean2):
    data = pd.read_csv('Dataset.csv')
    for row in range(len(data)):
        x = data['Data'].iloc[row]
        dataimage = cv2.imread(x, cv2.IMREAD_GRAYSCALE)
        moments2 = cv2.moments(dataimage)
        huMoments2 = cv2.HuMoments(moments2)
        
        for i in range(0, 7):
            y = -1 * (m.copysign(1.0, huMoments2[i]) * m.log10(abs(huMoments2[i])))
            huMoments2[i] = y
            print(huMoments2[i])
        mean = np.mean(huMoments2)
        print(mean)
        if round(mean, 6) == round(mean2, 6):
            print(mean2)
            print("Finger Print Matches ")
            cv2.imshow("Data Finger",dataimage)
            cv2.waitKey(0)

            break
        else:
            print("Finger print doesn't match")


o = imageMoments()
compare(o)
