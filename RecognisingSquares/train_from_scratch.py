#Loops through each gen, applies all images to each agent, then gathers scores.
#Instead of averaging, we will use a tanh function to map values between 0 and 1.

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


import random   #for randominsing agents
import csv  #for reading image csv files (generated in MATLAB, for now!)
import bubbleSort  #My File, with Functions, not a Class
import imageImport #My File, with Functions, not a Class
import time #for seeding the random function
import os   #for clearing the console screen
import math #For tanh function

middleNeurons = 3
lastNeurons = 1

def run(_numAgents, _squareFactor, _generations, _cuttOff, _badImagesStart):
    numAgents = _numAgents#100
    squareFactor = _squareFactor#0.5
    numShapes = 4
    imageSize = 6*6
    #middleNeurons = 3
    #lastNeurons = 1
    generations = _generations#200 #Number of Generations
    generation = 1  #Starting Generation
    cutOff = _cuttOff#20 #Number of Agents Moving to Next generation
    badImagesStart = _badImagesStart#4-1

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
                    #Simply each row adds to become the first neuron (goes through a function) (was averaging, now its tanh).
                    valueAt_k = (objectDataSL[k*6]+objectDataSL[(k*6)+1]+objectDataSL[(k*6)+2]+objectDataSL[(k*6)+3]+objectDataSL[(k*6)+4]+objectDataSL[(k*6)+5])
                    valueAt_k = float((1/2)*(math.tanh((1/2)*(valueAt_k-3))+1))
                    Layer1Nodes.append(valueAt_k)

                #print(Layer1Nodes)

                #There are 3 middle neurons
                Layer2Nodes = []
                for k in range(0,middleNeurons):
                    valueAt_k = ((Layer1Nodes[k*2]*NeuronLinks[k*2])+(Layer1Nodes[(k*2)+1]*NeuronLinks[(k*2)+1]))*2
                    valueAt_k = float((1/2)*(math.tanh((2)*(valueAt_k-1))+1))
                    Layer2Nodes.append(valueAt_k)

                #print(Layer2Nodes)

                #There is 1 single output.
                Layer3Nodes = []
                for k in range(0,lastNeurons):
                    valueAt_k = ((Layer2Nodes[k]*NeuronLinks[k+6])+(Layer2Nodes[k+1]*NeuronLinks[k+6+1])+(Layer2Nodes[k+2]*NeuronLinks[k+6+2]))*2
                    valueAt_k = float((1/2)*(math.tanh((1)*(valueAt_k-(3/2)))+1))
                    Layer3Nodes.append(valueAt_k)

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
        print(len(Agents[0]))
        #print(len(Agents))
    
        # THIS IS END OF LOOP
        os.system('cls')
        generation += 1

        if (generation == generations+1):
                print(AgentScores)
                print(GenerationScore)
                print(BestAgent)

    return BestAgent[0]


    #After the Loop
    print(AgentScores)
    print(GenerationScore)
    print(BestAgent)
    #print(BestAgent2)
    #print(BestAgent3)
    #print(AgentScores)
    #print(GenerationScore)
    #print(len(BestAgent[0]))
    #print(len(BestAgent2[0]))
    #print(len(BestAgent3[0]))

 