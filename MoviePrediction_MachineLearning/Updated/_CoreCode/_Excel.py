import csv

def readCSV(fileName):
    """Read Rows from an Excel (CSV) File"""
    output = []
    with open(fileName,newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            output.append(row[1:])
    return output

def writeCSV(fileName, data):
    """Write Rows to an Excel (CSV) File"""
    file = open(fileName,'w',newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)

def appendCSV(fileName, data):
    """Append Rows to an Excel (CSV) File"""
    file = open(fileName,'a',newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)


