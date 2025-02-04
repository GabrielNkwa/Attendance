from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import webbrowser
import time

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://192.168.1.6:27017/Attendance"
mongo = PyMongo(app)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/adlogin')
def adlogin():
    return render_template('adlogin.html')


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/staff_registration")
def staff_reg():
    return render_template("staff_registration.html")

@app.route("/")
def home():
    return render_template("index.html")









if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run('0.0.0.0', debug=True)