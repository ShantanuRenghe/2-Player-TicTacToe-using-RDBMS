import mysql.connector
global psw
psw = "shan1234"


# checks if user exists, if not adds to table
def check_user(username) :
	mydb = mysql.connector.connect(host="localhost", user="root", password=psw, database="TTT")
	mycursor = mydb.cursor()
	query = "select * from TTT_scores"
	mycursor.execute(query)
	result = mycursor.fetchall()
	exists = False
	for i in result :
		if i[0] == username.replace("\r", "") :
			exists = True
	if not exists :
		cmd = "insert into TTT_scores value(%s, %s, %s, %s)"
		addl = (username.replace("\r", ""), 0, 0, 0)
		mycursor.execute(cmd, addl)
		mydb.commit()


# updates players result into table
def update_result(result, username) :
	mydb = mysql.connector.connect(host="localhost", user="root", password=psw, database="TTT")
	mycursor = mydb.cursor()
	if result == "w" :
		query = "update TTT_scores set wins = wins + 1 where username = \"{}\";".format(username.replace("\r", ""))
		mycursor.execute(query)
	elif result == "d" :
		query = "update TTT_scores set draws = draws + 1 where username = \"{}\";".format(username.replace("\r", ""))
		mycursor.execute(query)
	elif result == "l" :
		query = "update TTT_scores set losses = losses + 1 where username = \"{}\";".format(username.replace("\r", ""))
		mycursor.execute(query)
	mydb.commit()


# displays scores of given user
def display_username(name) :
	mydb = mysql.connector.connect(host="localhost", user="root", password=psw, database="TTT")
	mycursor = mydb.cursor()
	mycursor.execute("select * from TTT_scores where username = \"{}\";".format(name.replace("\r", "")))
	result = mycursor.fetchall()
	try :
		if result[0][0] == name.replace("\r", ""):
			return result
	except IndexError:
		return "User doesn't exist."


# top 5 users with most wins
def high_score():
	table = []
	mydb = mysql.connector.connect(host="localhost", user="root", password=psw, database="TTT")
	mycursor = mydb.cursor()
	mycursor.execute("select * from TTT_scores order by wins desc;")
	result = mycursor.fetchall()
	mycursor.execute("select count(username) from TTT_scores;")
	size = mycursor.fetchall()
	for i in range(size[0][0]):
		table.append(result[i])
	return table
