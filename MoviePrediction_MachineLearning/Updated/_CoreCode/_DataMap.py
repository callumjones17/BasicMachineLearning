import math

def Percentage(value):
    """Maps 0-100% to 0-1"""
    return float(float(value)/100)

def Category(value,numCats):
    """Maps Categories to 0-1"""
    summation = 0
    for i in range(numCats):
        summation = summation + math.pow(2,i)
    return float(float(value)/summation)

def Length(value,maxTime):
    """Maps 0-MaxTime to 0-1"""
    return float(float(value)/maxTime)

#Currently Not Used
def numWords(value,maxWords):
    """Maps 0-MaxWords to 0-1"""
    return float(float(value)/maxWords)

def MapData(data,numCate,numMin):
    """Maps a list of Data"""
    output = []
    for dat in data:
        output.append([Percentage(dat[0]),Category(dat[1],numCate),Length(dat[2],numMin)])
    return output

def MapDataLine(data,numCate,numMin):
    """Maps a single line of Data"""
    output = []
    output.append([Percentage(data[0]),Category(data[1],numCate),Length(data[2],numMin)])
    return output






#### V2 ####
#Data changed a bit for V2. Instead of one category, there is now three.
#Relies on some of V1 Functions though
def MapDataV2(data,numCate,numMin):
    """Maps a list of Data for V2"""
    output = []
    for dat in data:
        output.append([Percentage(dat[0]),Length(dat[1],numCate),Length(dat[2],numCate),Length(dat[3],numCate),Length(dat[4],numMin)])
    return output

def MapDataV2Line(data,numCate,numMin):
    """Maps a list of Data for V2"""
    output = []
    output.append([Percentage(data[0]),Length(data[1],numCate),Length(data[2],numCate),Length(data[3],numCate),Length(data[4],numMin)])
    return output