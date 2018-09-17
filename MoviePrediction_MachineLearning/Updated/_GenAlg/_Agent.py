import random
import time

def createAgents(numOfAgents, numOfWeightings):
    """Randomly Create Agents Based on Number of Weightings"""
    random.seed(time.time() * 1000)
    Agents = []
    for i in range(numOfAgents):
        Weightings = []
        for k in range(numOfWeightings):
            Weightings.append(random.random())
        Agents.append(Weightings)
    return Agents

def createScoreArray(Agents):
    """Create an Array of Size Agents with all Zeros"""
    output = []
    for agent in Agents:
        output.append(0)
    return output