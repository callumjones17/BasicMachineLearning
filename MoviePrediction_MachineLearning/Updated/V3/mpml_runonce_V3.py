import _Excel as cFile
import _NeuralNet_V2 as nn
import _inputCollection as ic
import _DataMap as dm
import sys

agentFile = 'bestAgent.csv'
bestAgent = []
movieData = []
netmap = [1,3,1]

#Used across many programs
endFireFactor = 0.5
if (len(sys.argv) > 1):
    endFireFactor = float(sys.argv[1])
numCate = 12
numMin = 200

#Get Best again from File
bestAgent = cFile.readCSV(agentFile)[0]
#print(bestAgent)

#Make sure the agent is only floats
for i in range(len(bestAgent)):
    bestAgent[i] = float(bestAgent[i])

#Get information regarding movie to test
if (len(sys.argv) < 7):
    movieData.append(ic.getNum('Enter Rating/Score: ','Invalid Entry'))
    movieData.append(ic.getNum('Enter Category 1 Score: ','Invalid Entry'))
    movieData.append(ic.getNum('Enter Category 2 Score: ','Invalid Entry'))
    movieData.append(ic.getNum('Enter Category 3 Score: ','Invalid Entry'))
    movieData.append(ic.getNum('Enter Running Time: ','Invalid Entry'))
    movieData.append(ic.getNum('Enter Number of Words in Title: ','Invalid Entry'))
else:
    movieData.append(int(sys.argv[2]))
    movieData.append(int(sys.argv[3]))
    movieData.append(int(sys.argv[4]))
    movieData.append(int(sys.argv[5]))
    movieData.append(int(sys.argv[6]))
    movieData.append(int(sys.argv[7]))

#Map the data correctly
movieData = dm.MapDataV2Line(movieData,numCate,numMin)

#Get the result using the best agent
result = nn.runThroughNetworkOnce(movieData[0],bestAgent,netmap)
print(nn.getActualResult(endFireFactor,result))