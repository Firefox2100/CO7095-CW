from datetime import datetime
import mysql.connector
from uuid import uuid4

mydb = mysql.connector.connect(
  host="localhost",
  user="patrick",
  password="Wangyunze001021!",
  database="co7095"
)


def get_event(usertoken: str, date: str):
    selected_date = datetime.strptime(date, '%m-%d-%y')

    begin_date = "'" + str(selected_date.year) + "-" + str(selected_date.month) + "-" + str(selected_date.day) + "'"
    end_date = "'" + str(selected_date.year) + "-" + str(selected_date.month) + "-" + str(
        selected_date.day) + " 23：59：59'"

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE token = '" + usertoken + "';")
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return "User token error"

    sql_query = "SELECT * FROM events WHERE user = '" + usertoken + "' AND date >= " + begin_date + "AND date <" + end_date
    mycursor.execute(sql_query)
    myresult = mycursor.fetchall()

    return myresult


def add_event(usertoken: str, data):
    title = data['title']
    time = data['time']
    urgency = data['urgency']

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE token = '" + usertoken + "';")
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return "User token error"

    sql_query = "INSERT INTO events (date, title, urgency, user) VALUES ( %s , %s , %s , %s );"

    mycursor.execute(sql_query, (time, title, urgency, usertoken))
    mydb.commit()

    return True


def register(data):
    username = data['username']
    password = data['password']

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE `username` = '" + username + "';")
    myresult = mycursor.fetchall()

    for x in myresult:
        return 'User already exist'

    rand_token = str(uuid4())

    mycursor.execute("INSERT INTO users (username, password, token) VALUES ( %s , %s , %s);",
                     (username, password, rand_token))
    mydb.commit()
    return rand_token


def login(data):
    username = data['username']
    password = data['password']

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE username = '" + username + "';")
    myresult = mycursor.fetchall()

    for x in myresult:
        if password == x[2]:
            return x[3]
        else:
            return "Password error"

    return "User doesn't exist"
