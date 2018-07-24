#Basic bubble sorting functions.

import random #for random funcs
import _mymath #for clampEx

def sort(AgentScore, Agents):
    """Bubble Sort the Agent Scores"""
    maxIt = len(AgentScore)
    for i in range(0, maxIt):
        for j in range(0,maxIt-1):
            if AgentScore[j] > AgentScore[j+1]:
                swapValues(AgentScore,Agents,j,j+1)
    #print(AgentScore)
    return Agents

def sort_rev(AgentScore, Agents):
    """Bubble Sort the Agent Scores (Reverse Order)"""
    maxIt = len(AgentScore)
    for i in range(0, maxIt):
        for j in range(0,maxIt-1):
            if AgentScore[j] < AgentScore[j+1]:
                swapValues(AgentScore,Agents,j,j+1)
        #print(AgentScore)
    return Agents

def swapValues(AgentScore, Agents, _from, _to):
    """Swap Elements in an Array"""
    
    temp = AgentScore[_from]
    AgentScore[_from] = AgentScore[_to]
    AgentScore[_to] = temp

    tempAgent = Agents[_from]
    Agents[_from] = Agents[_to]
    Agents[_to] = tempAgent

    return Agents

def swapValuesOneArray(Agents, _from, _to):
    """Swap Elements in an Array"""
    
    temp = Agents[_from]
    Agents[_from] = Agents[_to]
    Agents[_to] = temp

    return Agents

def unsort(Agents):
    """Attempt to unbubble sort an array"""
    for i in range(0+1,len(Agents)-1):
        index = int(random.random()*len(Agents)-2)+1
        index2 = int(random.random()*len(Agents)-2)+1
        index2 = _mymath.clampEx(index2,index)
        Agents = swapValuesOneArray(Agents,index,index2)
    return Agents

def unsort(Agents, numSwaps):
    """Attempt to unbubble sort an array, specific number of swaps"""
    for i in range(numSwaps):
        index = int(random.random()*len(Agents)-2)+1
        index2 = int(random.random()*len(Agents)-2)+1
        index2 = _mymath.clampEx(index2,index)
        Agents = swapValuesOneArray(Agents,index,index2)
    return Agents

###THIS IS ONLY USED FOR GETTING AGENT FROM PROGRAM TO PROGRAM!!!
def reverseArrayOrder(array):
    #Reverses the Order of an Array
    output = []
    lenA = len(array)
    for i in range(lenA):
        output.append(array[lenA-1-i])
    return output