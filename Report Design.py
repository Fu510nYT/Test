from flask import Flask, render_template
import datetime

app = Flask(__name__, template_folder='./')

@app.route("/")
def home():
    info = []
    info.append("Patient Name: ")
    info.append("Cause: ")
    info.append("Gender: ")
    info.append("Allergies: ")
    info.append("Medical ID: ")
    info.append("Room Number: ")
    info.append("Medicine Serving Time: ")
    info.append("Medicine: ")

    s = "<style>.row { margin-bottom: 20px; }</style><div class='messagebox'>"

    for line in info:
        s += "<div class='row'>" + line + "</div>"
    s += "</div>"


    return s



@app.route("/render")
def page():
    return render_template('page.html')

app.run("127.0.0.1", debug=True)