import _Excel as cFile
import _NeuralNet as nn
import _inputCollection as ic
import _DataMap as dm

agentFile = 'bestAgent.csv'
bestAgent = []
movieData = []

#Used across many programs
endFireFactor = 0.5
numCate = 12
numMin = 200

#Get Best again from File
bestAgent = cFile.readCSV(agentFile)[0]
#print(bestAgent)

#Make sure the agent is only floats
for i in range(len(bestAgent)):
    bestAgent[i] = float(bestAgent[i])

#Get information regarding movie to test
movieData.append(ic.getNum('Enter Rating/Score: ','Invalid Entry'))
movieData.append(ic.getNum('Enter Category Score: ','Invalid Entry'))
movieData.append(ic.getNum('Enter Running Time: ','Invalid Entry'))
movieData.append(ic.getNum('Enter Number of Words in Title: ','Invalid Entry'))

#Map the data correctly
movieData = dm.MapDataLine(movieData,numCate,numMin)

#Get the result using the best agent
result = nn.runThroughNetworkWithAgent(movieData[0],bestAgent)
print(nn.getActualResult(endFireFactor,result))