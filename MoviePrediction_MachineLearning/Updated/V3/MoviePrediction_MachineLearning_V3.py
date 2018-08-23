#5-2-1 inputs are rating/score, cate1, cate2, cate3 and run time
import _Excel as cfile
import _Agent as ag
import _NeuralNet_V2 as nn
import _DataMap as dm
import _GeneticAlg as ga
import _bubbleSort as bs
import random
import time
import sys

#Can be put into funcion
numAgents = 40
generations = 500
endFireFactor = 0.5
if len(sys.argv) > 1:
    numAgents = int(sys.argv[1])
if len(sys.argv) > 2:
    generations = int(sys.argv[2])
if len(sys.argv) > 3:
    endFireFactor = float(sys.argv[3])

numSwaps = 5
if len(sys.argv) > 4:
    numSwaps = int(sys.argv[4])

layoutOfNetwork = [1,3,1]
numCate = 12
numMin = 200
resultPos = 6
minC = 0.4
maxC = 0.6
minCut = 0.3
maxCut = 0.7
mutModifier = 2
if (len(sys.argv)) > 5:
    mutModifier = int(sys.argv[5])
echoRes = 6

#Files
outputFile = 'testOut.csv'
bestAgentFile = 'bestAgent.csv'
dataInputFile = 'dataV2.csv'

#Number of nodes in each layer
n1 = 0
n2 = 1
n3 = 2
nW = 3

#Used only by the program
generation = 1
numRandomAgents = 0

#Setup Data File with Results and Data for ML
fullData = cfile.readCSV(dataInputFile)[1:]

#Map Data Appropriately
data = dm.MapDataV2(fullData,numCate,numMin)

#Calculate num of Weightings
netInfo = nn.setupNetwork(layoutOfNetwork)

#Setup the Agents
Agents = ag.createAgents(numAgents,netInfo[nW])
AgentScores = ag.createScoreArray(Agents)

generationResults = []
bestAgent = []
while generation != generations+1:
    random.seed(time.time() * 1000)
    movieId = -1
    movieResults = []
    for movie in data:
        movieId = movieId + 1
        agentId = -1
        AgentResults = []
        for agent in Agents:
            agentId = agentId + 1
            result = (nn.runThroughNetworkOnce(movie,agent,layoutOfNetwork))
            AgentScores[agentId] = AgentScores[agentId] + nn.workOutResult(fullData,resultPos,endFireFactor,movieId,result)
            AgentResults.append(nn.getActualResult(endFireFactor,result))
        movieResults.append([fullData[movieId][resultPos],movieId,AgentResults])


    #Sort Agents First
    Agents = bs.sort_rev(AgentScores,Agents)


    #Kill off poor performing Agents
    [Agents, cut, acScores] = ga.properSelection(Agents,AgentScores,len(data),minC,maxC)
    numBreed = int(ga.numToBreed(numAgents,len(Agents)))
    numRandomAgents = numAgents - len(Agents) - 2*numBreed
    bestAgent = Agents[0:2]


    #Unsort the Agents
    Agents = ga.bs.unsort(Agents,numSwaps)


    #Surviving Agents Breed to create more
    cutPoint = int(random.random()*((maxCut-minCut)+minCut)*len(Agents[0]))
    Agents = ga.singleCrossover(Agents,numBreed,cutPoint)


    #Create some Random New Agents
    Agents = ga.randomAgentsV3(Agents,numRandomAgents,netInfo[nW])


    #Randomly Mutate some Aspects of some Agents
    Agents = ga.gaMutation(Agents,mutModifier)


    print(str(generation) + ' : ' + str(len(data)) + ' : ' + str(AgentScores))    
    AgentScores = ag.createScoreArray(Agents)   
    generation = generation + 1
    generationResults.append([generation,movieResults])



#Complex method of saving the top 2 agents to a file. 
#0 is Appended because reading, the first column doesnt get read for some reason
bestAgent[0].append(0)
bestAgent[1].append(0)
bestAgent[0] = ga.bs.reverseArrayOrder(bestAgent[0])
cfile.writeCSV(bestAgentFile,bestAgent)

if (len(sys.argv) > echoRes):
    for gen in generationResults:
        print(gen[0])
        for mov in gen[1]:
            print(mov[0])
            print(mov[1])
            print(mov[2])