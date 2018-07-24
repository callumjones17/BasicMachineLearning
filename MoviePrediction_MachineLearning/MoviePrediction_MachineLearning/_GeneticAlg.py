import _bubbleSort as bs
import random
import time


#Cuttoff Stuff
def naturalSelection(Agents,AgentScores,numSurvivors):
    survivingAgents = []
    survivingAgents = bs.sort_rev(AgentScores,Agents)[0:numSurvivors]
    return survivingAgents

def properSelection(Agents,AgentScores,numSurvivors,maxScore):
    surAgents  = []
    surAgents = bs.sort_rev(AgentScores,Agents)
    lenAg = len(surAgents)
    normScores = surAgents
    accumScores = []
    normScore = 0
    #Step 1 - Normalise The Results, so they add up to 1.
    for score in AgentScores:
        normScore = normScore + score
    for agentId in range(lenAg):
        normScores[agentId] = float(AgentScores[agentId] / normScore)

    #print(normScores)

    #Step 2 - Sort Agents (They are already sorted)
    #Step 3 - Accumulated Results
    accumScores = normScores
    for i in range(1,len(normScores)):
        accumScores[i] = accumScores[i-1] + normScores[i]
    #print(accumScores)
    return Agents




#RandomStuff
def randomAgents(Agents, numAgents,numL1,numL2,numL3):
    newAgents = []
    newAgents = Agents
    for i in range(numAgents):
        newAgent = []
        for k in range((numL1*numL2)+(numL2*numL3)):
            newAgent.append(random.random())
        newAgents.append(newAgent)
        #print(len(newAgent))
    return newAgents




#Crossover Stuff (Breeding)
def breedAgents(Agents,num):
    #Breeds in a uniform pattern
    newAgents = []
    newAgents = Agents
    for i in range(num):
       newAgents.append(Agents[(i*2)][0:4]+Agents[(i*2)+1][4:len(Agents[0])])
    #print(newAgents)
    return newAgents

def breedAgentsEvenly(Agents,num):
    #Breeds more evenly
    newAgents = []
    newAgents = Agents
    lenAg = len(Agents[0])
    for i in range(int(num/2)):
       newAgents.append(Agents[(i*4)][0:4]+Agents[(i*4)+1][4:lenAg])
       newAgents.append(Agents[(i*4)+2][0:4]+Agents[(i*4)+3][4:lenAg])
    #print(newAgents)
    return newAgents

def singleCrossover(Agents,num,cutPoint):
    """Makes a Single Cut, Produces 2 new Agents from 2 Agents"""
    newAgents = []
    newAgents = Agents
    lenAg = len(Agents[0])
    for i in range(int(num/2)):
        newAgents.append(Agents[i*4][0:4]+Agents[(i*4)+1][4:lenAg])
        newAgents.append(Agents[(i*4)+1][0:4]+Agents[(i*4)][4:lenAg])
        newAgents.append(Agents[(i*4)+2][0:4]+Agents[(i*4)+3][4:lenAg])
        newAgents.append(Agents[(i*4)+3][0:4]+Agents[(i*4)+2][4:lenAg])
    return newAgents      




#Mutation Stuff
def mutateStrategically(Agents):
    #Warning: This Method only works for Weightings x 2 = Num(Agents)
    for i in range(12):
        Agents[i][i] = Agents[i][i] + 0.05
        Agents[i+12][i] = Agents[i+12][i] - 0.05
    return Agents

def inverseAgent(Agents, num):
    #Reverses num Agents
    agent = []
    lenAg = len(Agents[0])
    for i in range(num):
        for k in range(lenAg):
            agent.append(Agents[(i*5)+1][lenAg-k-1])
        Agents[(i*2)+1] = agent
        agent = []
    return Agents

def randomMutation(Agents,min,max):
    for i in range(min,max):
        Agents[int(random.random()*len(Agents))-1][int(random.random()*len(Agents[0]))-1] = random.random()
    return Agents

def gaMutation(Agents):
    """Mutate According to Research"""
    #Each Gene, from each Chromosone has a 1/L chance of mutation.
    #Where L is the length of the Chromosone
    random.seed(time.time())
    lenAg = len(Agents)
    lenGene = len(Agents[0])
    for agentId in range(lenAg):
        for geneId in range(lenGene):
            if ((random.random()*lenGene) < float(1/lenGene)):
                Agents[agentId][geneId] = 1 - Agents[agentId][geneId] 
    return Agents