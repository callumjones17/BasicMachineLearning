import mysql.connector

def writeToSqlTable(username,_password,_host,_database,table,fields,data):

    if (_password == ''):
        cnx = mysql.connector.connect(user=username,host=_host,database=_database)
    else:
        cnx = mysql.connector.connect(user=username,password=_password,host=_host,database=_database)

    cursor = cnx.cursor()

    add_data = ("INSERT INTO " + str(table)  + " " +  
               str(fields) +
               " VALUES (%s, %s)")

    column_data = data

    cnx.autocommit = True
    try:
        cursor.execute(add_data,column_data)
    except mysql.connector.IntegrityError:
        print('Check Primary Key isnt a duplicate, and data fits into correct Fields')

    #print(cursor.lastrowid)
    cursor.close()

    #print('something')
    cnx.close()
    return 0



def getWholeTable(username,_password,_host,_database,table):
    data = []

    if (_password == ''):
        cnx = mysql.connector.connect(user=username,host=_host,database=_database)
    else:
        cnx = mysql.connector.connect(user=username,password=_password,host=_host,database=_database)

    cursor = cnx.cursor()

    command = ("select * from "
               +str(table))

    cnx.autocommit = True
    cursor.execute(command)
    data = cursor.fetchall()
    cursor.close()

    cnx.close()

    return data
	
def runCommand(username,_password,_host,_database,table,command):
	if (_password == ''):
		cnx = mysql.connector.connect(user=username,host=_host,database=_database)
	else:
		cnx = mysql.connector.connect(user=username,password=_password,host=_host,database=_database)
	cursor = cnx.cursor()
	cnx.autocommit = True
	cursor.execute(command)
	data = cursor.fetchall()
	cursor.close()
	return data
	
def getBiggestId(username,_password,_host,_database,table):
	command = "SELECT Id FROM users"
	bigId = 0
	if (_password == ''):
		cnx = mysql.connector.connect(user=username,host=_host,database=_database)
	else:
		cnx = mysql.connector.connect(user=username,password=_password,host=_host,database=_database)
	cursor = cnx.cursor()
	cnx.autocommit = True
	cursor.execute(command)
	
	data = cursor.fetchall()
	cursor.close()
	
	for Id in data:
		if Id[0] > bigId:
			bigId = Id[0]
	
	return bigId