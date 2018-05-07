#Loops through each gen, applies all images to each agent, then gathers scores.

#Step 1:
#   Create Initial Agents                               Done
#Step 2:
#   Fill Agents with Random                             Done
#Step 3:
#   Start main loop                                     
#       Reco Image
#       Sort Agents by Score
#       Kill bottom 50% of Agents
#       Make Agents Breed
#       Give new Agents a Mutation
# There are 4 Shapes
#   -Triangle
#   -Rectangle
#   -Circle
#   -Line

# The first run of this application is only going to detect whether or not the image is of a square. ( A rating of between 1 and 10).

# Need Dictionary of Shapes and Corresponding Answers


import random
import csv
import bubbleSort  #My File, with Functions, not a Class
import imageImport #My File, with Functions, not a Class
import time
import os


numAgents = 80
squareFactor = 0.5
numShapes = 4
imageSize = 6*6
middleNeurons = 3
lastNeurons = 1
generations = 150 #Number of Generations
generation = 1  #Starting Generation
cutOff = 20 #Number of Agents Moving to Next generation
badImagesStart = 4

random.seed(time.time()*1000)

Agents = []
BestAgent = []
BestAgent2 = []
BestAgent3 = []

for i in range(0,numAgents):

    #print(i)    #debugging
    NeuronLinks = []
    #for i in range(0,imageSize*imageSize):
    #    agent.append(random.random())
    for i in range(0,6):
        NeuronLinks.append(random.random())
        #random.seed(time.time()*1000+10)
    for i in range(0,middleNeurons):
        NeuronLinks.append(random.random())
        #random.seed(time.time()*1000)
    Agents.append(NeuronLinks)
    #print(len(NeuronLinks))
#print(Agents)   #debugging

#print(Agents[0])
#print(Agents[1])


# Import Image Data
print('This many samples:')
images = imageImport.getImages()
print(len(images))


# Main Loop
while generation != generations+1:

    random.seed(time.time()*1000)
    #image = round(random.random()*(len(images)-1))
    #objectDataSL = images[image]

    os.system("cls")
    print('-----------')
    print('Generation:')
    print(generation)
    print('-----------')

    perImageAgentScores = []

    for image in images:
        AgentScores = []
        objectDataSL = image
        for agentNum in range(0,numAgents):
            NeuronLinks = Agents[agentNum]
            # First row connects to First Neuron, 2nd row to 2nd etc.
            Layer1Nodes = []
            for k in range (0,6):
                #for i in range(0,5):
                    # This adds the the rows toghether and averages them together to form the first neuron set.
                    # 2nd Option does the same but weighs it down.
                    #Layer1Nodes.append((objectDataSL[k*i]+objectDataSL[(k*i)+1]+objectDataSL[(k*i)+2]+objectDataSL[(k*i)+3]+objectDataSL[(k*i)+4]+objectDataSL[(k*i)+5])/6*2)
                    #FmN.append(((objectDataSL[k*i*6]*NeuronLinks[(k*i*6)])+(objectDataSL[(k*i*6)+1]*NeuronLinks[(k*i*6)+1])+(objectDataSL[(k*i*6)+2]*NeuronLinks[(k*i*6)+2])+(objectDataSL[(k*i*6)+3]*NeuronLinks[(k*i*6)+3])+(objectDataSL[(k*i*6)+4]*NeuronLinks[(k*i*6)+4])+(objectDataSL[(k*i*6)+5]*NeuronLinks[(k*i*6)+5]))/6)
                    # For now, use first option, if training is too hard, use 2nd option.
                Layer1Nodes.append((objectDataSL[k*6]+objectDataSL[(k*6)+1]+objectDataSL[(k*6)+2]+objectDataSL[(k*6)+3]+objectDataSL[(k*6)+4]+objectDataSL[(k*6)+5])/6*2)

            #print(Layer1Nodes)

            #There are 3 middle neurons
            Layer2Nodes = []
            for k in range(0,middleNeurons):
                Layer2Nodes.append(((Layer1Nodes[k*2]*NeuronLinks[k*2]+(Layer1Nodes[(k*2)+1]*NeuronLinks[(k*2)+1]))/2))

            #print(Layer2Nodes)

            #There is 1 single output.
            Layer3Nodes = []
            for k in range(0,lastNeurons):
                Layer3Nodes.append(((Layer2Nodes[k]*NeuronLinks[k+6])+(Layer2Nodes[k+1]*NeuronLinks[k+6+1])+(Layer2Nodes[k+2]*NeuronLinks[k+6+2]))/3*2)

            #print(Layer3Nodes)

            AgentScores.append(Layer3Nodes[0]) 
        perImageAgentScores.append(AgentScores) 
            #if Layer3Nodes[0] > squareFactor:
                #print('A Square!')
                #squareScore+=1
            #else:
                #print('Not a Square!')


    #print(perImageAgentScores)
    
    
    #Score Agents:
    AgentScores = []
    for agent in range(0,len(Agents)):
        agentScore = 0
        GenerationScore = []
        for image in range(0,badImagesStart):
            if perImageAgentScores[image][agent] > squareFactor:
                agentScore += 1
                GenerationScore.append('Square')
            else:
                GenerationScore.append('Not Square')
        for image in range(badImagesStart,len(images)):
            if perImageAgentScores[image][agent] < squareFactor:
                agentScore += 1
                GenerationScore.append('Not Square')
            else:
                GenerationScore.append('Square')
        AgentScores.append(agentScore)

    # Sort Agents Based on Score
    #print(bubbleSort.sort(AgentScores, Agents))
    sortedAgents = bubbleSort.sort(AgentScores,Agents)
    #print(AgentScores)
    #print(sortedAgents)
    BestAgent = sortedAgents[-1:]
    BestAgent2 = sortedAgents[-2:-1]
    BestAgent3 = sortedAgents[-3:-2]
    

    # Kill low scoring agents
    AliveAgents = sortedAgents[-cutOff:]


    # Breed and Mutate Agents
    NewAgents = []
    for i in range(0,int((numAgents-(numAgents-cutOff))/2)):
        newAgent = AliveAgents[i*2][0:5] + AliveAgents[(i*2)+1][5:len(AliveAgents[0])]
        NewAgents.append(newAgent)

    #Mutation
    NewAgents[int(random.random()*(len(NewAgents)-2))][int(random.random()*(len(NewAgents[0])-2))] = random.random()
    NewAgents[int(random.random()*(len(NewAgents)-2))][int(random.random()*(len(NewAgents[0])-2))] = random.random()
    #NewAgents[int(random.random()*len(NewAgents))-1][int(random.random()*len(NewAgents[0]))] = random.random()

    #Missing Agents
    newAgent = []
    for k in range(0,numAgents-(len(NewAgents)+len(AliveAgents))):
        for i in range(0,43-34):
            newAgent.append(random.random())
            #random.seed(time.time()*1000)
        NewAgents.append(newAgent)

    Agents = NewAgents + AliveAgents
    #print(len(Agents))
    
    # THIS IS END OF LOOP
    generation += 1

#After the Loop
print(AgentScores)
print(GenerationScore)
print(BestAgent)
print(BestAgent2)
print(BestAgent3)