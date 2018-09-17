import _mymath as cma
import math

def setupNetwork(networkMap):
    """Work out how many Nuerons and total Weights are required for each Layer"""
    numL1 = 0
    numL2 = 0
    numL3 = 0
    numWe = 0
    counter = 0
    for i in range(len(networkMap)):
        numWe = numWe + networkMap[i]
        numL2 = numL2 + 1
        numL1 = numL1 + networkMap[i]
    numL3 = 1
    numWe = numWe + (numL2*numL3)
    return [numL1,numL2,numL3,numWe]


def runThroughNetworkOnce(data,agent,NetworkMap):
    """"Run One Agent Through All Data Once Returns Result."""
    Layer2Nodes = []
    Layer3Nodes = []
    sum = 0
    counter = 0

    for i in NetworkMap:
        sum = 0
        for j in range(i):
            sum = sum + data[counter] * agent[counter]
            counter = counter+1
        Layer2Nodes.append(nodeFire(sum,i))

    sum = 0
    for i in Layer2Nodes:
        sum = sum + (i * agent[counter])
        counter = counter+1
    Layer3Nodes.append(nodeFire(sum,len(Layer2Nodes)))

    return Layer3Nodes[0]

def nodeFire(input,numL):
    """"Tanh Function to Range Limit all Incomming Data"""
    output =  float((1/2)*(math.tanh((float(1/(numL/4)))*(input-(float(numL/2))))+1))
    return output

def workOutResult(fullDataSet,resultRow,fireFactor,movieId,result):
    """Returns a 1 if Matches Movie and 0 if Not"""
    if (result > fireFactor):
#       print('Y')
        if (fullDataSet[movieId][resultRow] == 'Y'):
            result = 1
#           print("Correct")
        else:
            result = 0
#           print("Wrong")
    else:
 #      print('N')
        if (fullDataSet[movieId][resultRow] == 'N'):
            result = 1
#           print("Correct")
        else:
            result = 0
#           print("Wrong")
    return result

def getActualResult(fireFactor,result):
    """A number is no good to the user, returns Y or N"""
    resultAct = 'X'
    if (result > fireFactor):
#       print('Y')
        resultAct = 'Y'
    else:
 #      print('N')
        resultAct = 'N'
    return resultAct