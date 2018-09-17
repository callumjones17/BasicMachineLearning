import _mymath as cma
import math

def setupNetwork(numLayer1,numLayer2,numLayer3):
    return (numLayer1*numLayer2) + (numLayer2*numLayer3)

def runThroughNetworkWithAgent(data,agent,numL1,numL2,numL3):
    """Take an Agent through all the Data, set up only for an x-x-x network"""
    Layer1Nodes = []
    Layer2Nodes = []
    Layer3Nodes = []

    #Layer 1:
    #WARNING: THIS SECTION IS hardcoded for a x-x-x netowrk!!!!
    for dat in data:
        Layer1Nodes.append(dat)

    #Layer 2:
    for node in range(numL2):
        weightedNode = 0    #(Layer1Nodes[0] * agent[node]) + (Layer1Nodes[0+1] * agent[node+1]) + (Layer1Nodes[0+2] * agent[node+2])
        for i in range(numL1):
            weightedNode = weightedNode + (Layer1Nodes[0+i] * agent[(node*numL1)+i])
        newNode = float((2)*(math.tanh((float(1/(numL1/4)))*(weightedNode-(float(numL1/2))))+1))
        newNode = cma.clamp(newNode,1)
        Layer2Nodes.append(newNode)

    #Layer 3:
    for node in range(numL3):
        weightedNode = 0    #(Layer2Nodes[0] * agent[node+(numL1*numL2)]) + (Layer2Nodes[0+1] * agent[node+1+(numL1*numL2)])
        for i in range(numL2):
            weightedNode = weightedNode + (Layer2Nodes[0+i] * agent[node+(numL1*numL2)+i])
        newNode = float((2)*(math.tanh((float(1/(numL2/4)))*(weightedNode-(float(numL2/2))))+1))
        newNode = cma.clamp(newNode,1)
        Layer3Nodes.append(newNode)

    #Return Just the one value for the time being
    return Layer3Nodes[0]


def runThroughNetworkWithAgentWithFireFactor(data,agent,fireFactor):
    """Take an Agent through all the Data, set up only for an x-x-x network, with fire factor"""
    Layer1Nodes = []
    numL1 = 3
    Layer2Nodes = []
    numL2 = 2
    Layer3Nodes = []
    numL3 = 1

    #Layer 1:
    #WARNING: THIS SECTION IS hardcoded for a x-x-x netowrk!!!!
    for dat in data:
        Layer1Nodes.append(dat)

    #Layer 2:
    for node in range(numL2):
        weightedNode = 0    #(Layer1Nodes[0] * agent[node]) + (Layer1Nodes[0+1] * agent[node+1]) + (Layer1Nodes[0+2] * agent[node+2])
        for i in range(numL1):
            weightedNode = weightedNode + (Layer1Nodes[0+i] * agent[(node*numL1)+i])
        newNode = float((2)*(math.tanh((float(1/(numL1/4)))*(weightedNode-(float(numL1/2))))+1))
        if newNode >= fireFactor:
            newNode = cma.clamp(newNode,1)
        else:
            newMode = 0
        Layer2Nodes.append(newNode)

    #Layer 3:
    for node in range(numL3):
        weightedNode = 0    #(Layer2Nodes[0] * agent[node+(numL1*numL2)]) + (Layer2Nodes[0+1] * agent[node+1+(numL1*numL2)])
        for i in range(numL2):
            weightedNode = weightedNode + (Layer2Nodes[0+i] * agent[node+(numL1*numL2)+i])
        newNode = float((2)*(math.tanh((float(1/(numL2/4)))*(weightedNode-(float(numL2/2))))+1))
        if newNode >= fireFactor:
            newNode = cma.clamp(newNode,1)
        else:
            newMode = 0
        Layer3Nodes.append(newNode)

    #Return Just the one value for the time being
    return Layer3Nodes[0]


def workOutResult(fullDataSet,resultRow,fireFactor,movieId,result):
    """Based on the result, work out it network was correct, returns 0 or 1"""
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
    """Get actual result - Easier for Humans to understand, returns Y or N"""
    resultAct = 'X'
    if (result > fireFactor):
#       print('Y')
        resultAct = 'Y'
    else:
 #      print('N')
        resultAct = 'N'
    return resultAct