# Loops through each gen, picks an image, applies to all agents.





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


numAgents = 100
squareFactor = 0.7
numShapes = 4
imageSize = 6*6
middleNeurons = 3
lastNeurons = 1
generations = 100 #Number of Generations
generation = 1  #Starting Generation
cutOff = 60 #Number of Agents Moving to Next generation

Agents = []
for i in range(0,numAgents):

    #print(i)    #debugging
    NeuronLinks = []
    #for i in range(0,imageSize*imageSize):
    #    agent.append(random.random())
    for i in range(0,6):
        NeuronLinks.append(random.random())
        random.seed(time.time()*1000)
    for i in range(0,imageSize):
        NeuronLinks.append(random.random())
        random.seed(time.time()*1000)
    for i in range(0,lastNeurons):
        NeuronLinks.append(random.random())
        random.seed(time.time()*1000)
    Agents.append(NeuronLinks)
    #print(len(NeuronLinks))
#print(Agents)   #debugging


# Import Image Data
print('This many samples:')
images = imageImport.getImages()
print(len(images))


# Main Loop
while generation != generations+1:

    random.seed(time.time()*1000)
    image = round(random.random()*(len(images)-1))
    objectDataSL = images[image]

    print('-----------')
    print('Generation:')
    print(generation)
    print('Image:')
    print(image)
    print('-----------')
    
    # Recognise Images from a Dictionary, just one image for now. For all Agents
    #Score of 0.5+ fires a neuron (What are you on about??)
    
    AgentScores = []
    squareScore = 0
    for agentNum in range(0,numAgents):
        NeuronLinks = Agents[agentNum]
        # First row connects to First Neuron, 2nd row to 2nd etc.
        Layer1Nodes = []
        for k in range (1,6):
            for i in range(0,5):
                # This adds the the rows toghether and averages them together to form the first neuron set.
                # 2nd Option does the same but weighs it down.
                Layer1Nodes.append((objectDataSL[k*i]+objectDataSL[(k*i)+1]+objectDataSL[(k*i)+2]+objectDataSL[(k*i)+3]+objectDataSL[(k*i)+4]+objectDataSL[(k*i)+5])/6*2)
                #FmN.append(((objectDataSL[k*i*6]*NeuronLinks[(k*i*6)])+(objectDataSL[(k*i*6)+1]*NeuronLinks[(k*i*6)+1])+(objectDataSL[(k*i*6)+2]*NeuronLinks[(k*i*6)+2])+(objectDataSL[(k*i*6)+3]*NeuronLinks[(k*i*6)+3])+(objectDataSL[(k*i*6)+4]*NeuronLinks[(k*i*6)+4])+(objectDataSL[(k*i*6)+5]*NeuronLinks[(k*i*6)+5]))/6)
                # For now, use first option, if training is too hard, use 2nd option.

        #There are 3 middle neurons
        Layer2Nodes = []
        for k in range(0,middleNeurons):
            Layer2Nodes.append(((Layer1Nodes[k+2]*NeuronLinks[35+k]+(Layer1Nodes[(k+2)+1]*NeuronLinks[35+k+1]))/2))

        #There is 1 single output.
        Layer3Nodes = []
        for k in range(0,lastNeurons):
            Layer3Nodes.append(((Layer2Nodes[k]*NeuronLinks[35+middleNeurons+k])+(Layer2Nodes[k+1]*NeuronLinks[35+middleNeurons+k+1])+(Layer2Nodes[k+2]*NeuronLinks[35+middleNeurons+k+2]))/3*2)

        AgentScores.append(Layer3Nodes[0])  
        if Layer3Nodes[0] > squareFactor:
            #print('A Square!')
            squareScore+=1
        #else:
            #print('Not a Square!')
    print('     SquareScore:')
    print(squareScore)





    # Sort Agents Based on Score
    #print(bubbleSort.sort(AgentScores, Agents))
    if image < 5:
        sortedAgents = bubbleSort.sort(AgentScores,Agents)
    else:
        sortedAgents = bubbleSort.sort_rev(AgentScores,Agents)
    #print(sortedAgents)
    

    # Kill low scoring agents
    if squareScore > int(numAgents/5) and image < 5:
        cutOff = int(0.6*numAgents)
    elif squareScore == 0 and image < 5:
        cutOff = 0
    elif squareScore == 100 and image > 4:
        cutOff = 0
    else:
        cutOff = 30
    
        
    AliveAgents = sortedAgents[-cutOff:]

    # Breed and Mutate Agents
    NewAgents = []
    for i in range(0,int((numAgents-(numAgents-cutOff))/2)):
        newAgent = AliveAgents[i*2][0:3] + AliveAgents[(i*2)+1][3:6] + AliveAgents[i*2][6:22] + AliveAgents[(i*2)+1][22:40] + AliveAgents[i*2][40:42] + AliveAgents[(i*2)+1][42:]
        NewAgents.append(newAgent)

    #Missing Agents
    newAgent = []
    for k in range(0,numAgents-(len(NewAgents)+len(AliveAgents))):
        for i in range(0,43):
            newAgent.append(random.random())
            random.seed(time.time()*1000)
        NewAgents.append(newAgent)

    Agents = NewAgents + AliveAgents
    #print(len(Agents))
    

    print('-----------')
    print('-----------')


    
    # THIS IS END OF LOOP
    generation += 1