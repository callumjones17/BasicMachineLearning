import _bubbleSort as bs
import random
import time


#Number to Breed
def numToBreed(numAgents, numSurv):
    num = 0
    if (numAgents-numSurv)%2 == 0:
        num = (numAgents-numSurv)/2
    else:
        num = (numAgents-numSurv-1)/2
    if (num%2 == 0):
        num = num/2
    else:
        num = (num-1)/2
    return num


#Cuttoff Stuff
def naturalSelection(Agents,AgentScores,numSurvivors):
    survivingAgents = []
    survivingAgents = bs.sort_rev(AgentScores,Agents)[0:numSurvivors]
    return survivingAgents

def properSelection(Agents,AgentScores,maxScore,minC,maxC):
    lenAg = len(Agents)
    normScores = []
    accumScores = []
    normScore = 0
    #Step 1 - Normalise The Results, so they add up to 1.
    for score in AgentScores:
        normScore = normScore + score
    for score in range(lenAg):
        #print(agentId)
        normScores.append(float(score / normScore))

    #Step 2 - Sort Agents (They are already sorted)
    #Step 3 - Accumulated Results
    accumScores = normScores
    for i in range(1,len(normScores)):
        accumScores[i] = accumScores[i-1] + normScores[i]
    #print(accumScores)

    #Step 4 Generate a number between min and max for the cutoff.
    cutoff = (random.random()*(maxC-minC)) + minC

    #Step 5 Cutoff 
    for index in range(len(accumScores)):
        if accumScores[index] > cutoff:
            cutoff = index
            break
    Agents = Agents[0:cutoff]
    #Return
    return [Agents,cutoff,accumScores]









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

def randomAgentsV3(Agents, numAgents,numW):
    newAgents = []
    newAgents = Agents
    for i in range(numAgents):
        newAgent = []
        for k in range(numW):
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
    #newAgents = []
#    newAgents = Agents
    lenAg = len(Agents[0])
    for i in range(int(num)):
        #try:
            #newAgents.append(Agents[i*2][0:cutPoint]+Agents[(i*2)+1][cutPoint:lenAg])
            Agents.append(Agents[i*2][0:cutPoint]+Agents[(i*2)+1][cutPoint:lenAg])
        #except IndexError:
            #print('issue - 1')
        #try:
            #newAgents.append(Agents[(i*2)+1][0:cutPoint]+Agents[(i*2)][cutPoint:lenAg])
            Agents.append(Agents[(i*2)+1][0:cutPoint]+Agents[(i*2)][cutPoint:lenAg])
        #except IndexError:
            #print('issue - 2')
    return Agents      




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

def gaMutation(Agents, numRunThroughs):
    """Mutate According to Research"""
    #Each Gene, from each Chromosone has a 1/L chance of mutation.
    #Where L is the length of the Chromosone
    random.seed(time.time())
    lenAg = len(Agents)
    lenGene = len(Agents[0])
    for run in range(numRunThroughs):
        for agentId in range(lenAg):
            for geneId in range(lenGene):
                if ((random.random()*lenGene) < float(1/lenGene)):
                    Agents[agentId][geneId] = 1 - Agents[agentId][geneId] 
    return Agents