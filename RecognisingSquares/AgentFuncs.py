import train_from_scratch #for some referenced data
import math #for tanh

def test(Agent,image):
    """Test an Agents ability against an Image"""
    
    objectDataSL = image
    middleNeurons = train_from_scratch.middleNeurons
    lastNeurons = train_from_scratch.lastNeurons
    NeuronLinks = Agent

    Layer1Nodes = []
    result = []

    for k in range (0,6):
        #Simply each row adds to become the first neuron (goes through a function) (was averaging, now its tanh).
        valueAt_k = (objectDataSL[k*6]+objectDataSL[(k*6)+1]+objectDataSL[(k*6)+2]+objectDataSL[(k*6)+3]+objectDataSL[(k*6)+4]+objectDataSL[(k*6)+5])
        valueAt_k = float((1/2)*(math.tanh((1/2)*(valueAt_k-3))+1))
        Layer1Nodes.append(valueAt_k)
    #print(Layer1Nodes)

    #There are 3 middle neurons
    Layer2Nodes = []
    for k in range(0,middleNeurons):
        valueAt_k = ((Layer1Nodes[k*2]*NeuronLinks[k*2])+(Layer1Nodes[(k*2)+1]*NeuronLinks[(k*2)+1]))*2
        valueAt_k = float((1/2)*(math.tanh((2)*(valueAt_k-1))+1))
        Layer2Nodes.append(valueAt_k)

    #print(Layer2Nodes)

    #There is 1 single output.
    Layer3Nodes = []
    for k in range(0,lastNeurons):
        valueAt_k = ((Layer2Nodes[k]*NeuronLinks[k+6])+(Layer2Nodes[k+1]*NeuronLinks[k+6+1])+(Layer2Nodes[k+2]*NeuronLinks[k+6+2]))*2
        valueAt_k = float((1/2)*(math.tanh((1)*(valueAt_k-(3/2)))+1))
        Layer3Nodes.append(valueAt_k)

    if Layer3Nodes[0] > 0.5:
        result.append('Square')
    else:
        result.append('Not Square')

    result.append(Layer3Nodes[0])

    return result


def saveToFile(Agent,fileName):
    """Save an Agent to a file"""
    with open(fileName, 'w') as file:
        for nl in Agent:
            file.write(str(nl)+'\n') 

def openFromFile(fileName):
    """Open an Agent from a file"""
    Agent = []
    with open(fileName) as file:
        fileLines = file.readlines()
    for nl in fileLines:
        Agent.append(float(nl))
    return Agent
