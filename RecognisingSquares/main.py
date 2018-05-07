import train_from_scratch
import AgentFuncs
import imageImport

Agent = []

Agent = train_from_scratch.run(150,0.5,5000,25,3)
print(Agent)
#AgentFuncs.saveToFile(Agent,'agent.nl')


#Agent = AgentFuncs.openFromFile('agent.nl')
#image = imageImport.singleImage('cross.csv')
#print(AgentFuncs.test(Agent,image))
