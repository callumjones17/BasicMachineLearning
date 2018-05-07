#Basic bubble sorting functions.

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