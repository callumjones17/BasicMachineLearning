import csv

def readCSV(fileName):
    output = []
    with open(fileName,newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            output.append(row[1:])
    return output

def writeCSV(fileName, data):
    file = open(fileName,'w',newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)

def appendCSV(fileName, data):
    file = open(fileName,'a',newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)


