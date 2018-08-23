import _SqlConnector as msql
import sys

username = 'callum'
password = ''
host = '127.0.0.1'
db = 'test'
table = 'users'

if (len(sys.argv)) > 1:
	returnedData = msql.runCommand(username,password,host,db,table,sys.argv[1])
	print(returnedData)
else:
	#msql.writeToSqlTable(username,password,host,db,table,'(id, name)',(6,'john 2'))
	returnedData = msql.getBiggestId(username,password,host,db,table)
	print(returnedData)

