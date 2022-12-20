from flask import Flask, url_for, request, render_template, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="192.168.0.87",
    user="phpmyadmin",
    password="admin",
    database="test"
)

mycursor = mydb.cursor(buffered = True)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/table", methods = ["POST"])

def table():
    anrede = request.form["anrede"]
    vorname = request.form["vorname"]
    nachname = request.form["nachname"]
    sql = f"INSERT INTO test (anrede, vorname, nachname, bild) VALUES (%s, %s, %s, %s)"
    val = (anrede, vorname, nachname, "")
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM test")
    data = mycursor.fetchall()
    mydb.commit()

    return render_template("table.html", data=data)

if __name__ == "__main__":
    app.run(debug = True)