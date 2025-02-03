from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import webbrowser
import time

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://192.168.1.6:27017/Attendance"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("home.py")

@app.route("/register", methods=['GET','POST'])
def act1():
    nm = request.form.get("name")
    sid = request.form.get("staff_id")
    dir = request.form.get("directorate")
    pspt1 = request.files.get("pspt1")
    pspt2 = request.files.get("pspt2")
    pspt3 = request.files.get("pspt3")
    pspt4 = request.files.get("pspt4")
    pspt5 = request.files.get("pspt5")
    
    mongo.save_file()
    data = {"Name": nm,"Staff ID":sid, "Directorate":dir, "Passport 1":pspt1.filename, "Passport 2":pspt2.filename, "Passport 3":pspt3.filename, "Passport 4":pspt4.filename, "Passport 5":pspt5.filename}
    mongo.db.USERS.insert_one(data)
    return render_template("test_play.html")

@app.route("/show")
def shh():
    data = mongo.db.USERS.find()
    data = list(data)
    return render_template('report_page', info=data)


if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run('0.0.0.0', debug=True)