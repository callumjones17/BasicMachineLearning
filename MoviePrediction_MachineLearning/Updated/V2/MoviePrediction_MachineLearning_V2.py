#5-2-1 inputs are rating/score, cate1, cate2, cate3 and run time
import _Excel as cfile
import _Agent as ag
import _NeuralNet as nn
import _DataMap as dm
import _GeneticAlg as ga
import random
import time

#Can be put into funcion
generations = 500
numAgents = 40
numSwaps = 7
numSurvivors = 24
numBreed = 12
numRandomAgents = 4
endFireFactor = 0.5
numCate = 12
numMin = 200
minMut = 1
maxMut = 25
resultPos = 6
outputFile = 'testOut.csv'
bestAgentFile = 'bestAgent.csv'
dataInputFile = 'dataV2.csv'

#Number of nodes in each layer
numL1 = 5
numL2 = 2
numL3 = 1

#Used only by the program
generation = 1
numOfWeightings = 0

#Setup Data File with Results and Data for ML
fullData = cfile.readCSV(dataInputFile)[1:]

#Map Data Appropriately
data = dm.MapDataV2(fullData,numCate,numMin)

#Calculate num of Weightings
numOfWeightings = nn.setupNetwork(numL1,numL2,numL3)

#Setup the Agents
Agents = ag.createAgents(numAgents,numOfWeightings)
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
            result = (nn.runThroughNetworkWithAgent(movie,agent,numL1,numL2,numL3))
            AgentScores[agentId] = AgentScores[agentId] + nn.workOutResult(fullData,resultPos,endFireFactor,movieId,result)
            AgentResults.append(nn.getActualResult(endFireFactor,result))
        movieResults.append([fullData[movieId][resultPos],movieId,AgentResults])


    #Kill off poor performing Agents
    Agents = ga.naturalSelection(Agents,AgentScores,numSurvivors)
    #Agents = ga.properSelection(Agents,AgentScores,numSurvivors,9)
    bestAgent = Agents[0:2]

    #Create some Random New Agents
    Agents = ga.randomAgents(Agents,numRandomAgents,numL1,numL2,numL3)

    #Unsort the Agents
    Agents = ga.bs.unsort(Agents,numSwaps)

    #Surviving Agents Breed to create more
    Agents = ga.breedAgents(Agents,numBreed)
    #Agents = ga.singleCrossover(Agents,numBreed/2,0)

    #Randomly Mutate some Aspects of some Agents
    Agents = ga.gaMutation(Agents)

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