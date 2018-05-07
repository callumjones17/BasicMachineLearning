# Import Image Data
# Image is defined as a 6x6 csv file. Will be drawn in paint and transfered to csv (MATLAB).

import csv

def getImages():
    """Read Excel Files and Store in a List of Lists"""
    images = []

    imageData = csv.reader(open('square.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    #imageData = csv.reader(open('square_2.csv','r'))
    #objectData = []
    #for row in imageData:
    #    objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    #objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    #images.append(objectDataSL)

    imageData = csv.reader(open('square_med_1.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('square_med_2.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('Circle.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('Circle_2.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('Triangle.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('Triangle_2.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('cross.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    imageData = csv.reader(open('line.csv','r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    objectDataSL = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    images.append(objectDataSL)

    return images

def singleImage(fileName):
    imageData = csv.reader(open(fileName,'r'))
    objectData = []
    for row in imageData:
        objectData.append([float(row[0])/255,float(row[1])/255,float(row[2])/255,float(row[3])/255,float(row[4])/255,float(row[5])/255])
    image = objectData[0] + objectData[1] + objectData[2] + objectData[3] + objectData[4] + objectData[5]
    return image