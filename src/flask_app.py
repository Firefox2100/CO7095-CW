from flask import *
import mysql.connector
from datetime import datetime
from uuid import uuid4


mydb = mysql.connector.connect(
  host="localhost",
  user="dbadmin",
  password="adminpassword",
  database="co7095"
)

app = Flask(__name__)


@app.route('/events/<usertoken>/<date>', methods=["GET"])
def get_events(usertoken, date):
    try:
        selected_date = datetime.strptime(date, '%m-%d-%y')

        begin_date = "'" + str(selected_date.year) + "-" + str(selected_date.month) + "-" + str(selected_date.day) + "'"
        end_date = "'" + str(selected_date.year) + "-" + str(selected_date.month) + "-" + str(selected_date.day) + " 23：59：59'"

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE 'token' = '" + usertoken + "'")
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return "User token error", 403

        sql_query = "SELECT * FROM events WHERE user = '" + usertoken + "' AND date >= " + begin_date + "AND date <" + end_date
        mycursor.execute(sql_query)
        myresult = mycursor.fetchall()

        return jsonify(myresult), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/add/<usertoken>', methods=['POST'])
def add_event(usertoken):
    try:
        data = request.get_json()

        temp = json.loads(data)

        title = temp['title']
        time = temp['time']
        urgency = temp['urgency']

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE `token` = `" + usertoken + "`")
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return "User token error", 403
        
        sql_query = "INSERT INTO `events`(`date`, `title`, `urgency`, `user`) VALUES ( %s , %s , %s , %s );"

        mycursor.execute(sql_query, (time, title, urgency, usertoken))
        return 'Success', 200

    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        temp = json.loads(data)

        username = temp['username']
        password = temp['password']

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE `username` = `" + username + "`")
        myresult = mycursor.fetchall()

        for x in myresult:
            return 'User already exist', 403
        
        rand_token = uuid4()

        mycursor.execute("INSERT INTO `users`(`username`, `password`, `token`) VALUES ( %s , %s , %s , %s );", (username, password, rand_token))
        return 'Success', 200

    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        temp = json.loads(data)

        username = temp['username']
        password = temp['password']

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE 'username' = '" + username + "'")
        myresult = mycursor.fetchall()

        for x in myresult:
            if password == x[2]:
                return x[3], 200
            else:
                return "Password error", 403

        return "User doesn't exist", 403

    except Exception as e:
        return f"An Error Occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
