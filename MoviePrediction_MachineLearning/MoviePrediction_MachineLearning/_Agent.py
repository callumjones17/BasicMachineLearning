import random
import time

def createAgents(numOfAgents, numOfWeightings):
    random.seed(time.time() * 1000)
    Agents = []
    for i in range(numOfAgents):
        Weightings = []
        for k in range(numOfWeightings):
            Weightings.append(random.random())
        Agents.append(Weightings)
    return Agents

def createScoreArray(Agents):
    output = []
    for agent in Agents:
        output.append(0)
    return output