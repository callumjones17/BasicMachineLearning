import _Excel as cfile
import _Agent as ag
import _NeuralNet as nn
import _DataMap as dm
import _GeneticAlg as ga
import random
import time

#Can be put into funcion
generations = 500
numAgents = 30
numSwaps = 7
numSurvivors = 15
numBreed = 10
numRandomAgents = 5
endFireFactor = 0.5
numCate = 12
numMin = 200
minMut = 1
maxMut = 5
resultPos = 4
outputFile = 'testOut.csv'
bestAgentFile = 'bestAgent.csv'

#Number of nodes in each layer
numL1 = 3
numL2 = 2
numL3 = 1

#Used only by the program
generation = 1
numOfWeightings = 0

#Setup Data File with Results and Data for ML
fullData = cfile.readCSV('Data.csv')[1:]

#Map Data Appropriately
data = dm.MapData(fullData,numCate,numMin)

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
            result = (nn.runThroughNetworkWithAgent(movie,agent))
            AgentScores[agentId] = AgentScores[agentId] + nn.workOutResult(fullData,resultPos,endFireFactor,movieId,result)
            AgentResults.append(nn.getActualResult(endFireFactor,result))
        movieResults.append([fullData[movieId][resultPos],movieId,AgentResults])


    #Kill off poor performing Agents
    Agents = ga.naturalSelection(Agents,AgentScores,numSurvivors)
    bestAgent = Agents[0:2]

    #Create some Random New Agents
    Agents = ga.randomAgents(Agents,numRandomAgents,numL1,numL2,numL3)

    #Unsort the Agents
    Agents = ga.bs.unsort(Agents,numSwaps)

    #Surviving Agents Breed to create more
    Agents = ga.breedAgents(Agents,numBreed)

    #Randomly Mutate some Aspects of some Agents
    Agents = ga.randomMutation(Agents,minMut,maxMut)

    print(str(generation) + ' : ' + str(len(data)) + ' : ' + str(AgentScores))    
    AgentScores = ag.createScoreArray(Agents)   
    generation = generation + 1
    generationResults.append([generation,movieResults])



bestAgent[0].append(0)
bestAgent[1].append(0)
bestAgent[0] = ga.bs.reverseArrayOrder(bestAgent[0])
cfile.writeCSV(bestAgentFile,bestAgent)

#print('-------------------')
#print('-------------------')
#print(generationResults)
#cfile.writeCSV('testData.csv',generationResults)

#for genRes in generationResults:
#        cfile.appendCSV(outputFile,['Generation',genRes[0]])
#        for i in range(len(genRes[1])-1):
#            cfile.appendCSV(outputFile,genRes[0][1][i])