#!/usr/bin/env python

import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def test():
    f = open("/home/mustar/voice_records.txt", "r")
    lines = f.readlines()
    f.close()
    s = "Patient Name: "
    s += "<style>.row { margin-bottom: 20px; }</style><div class='messagebox'>"



    for line in lines:
        s += "<div class='row'>" + line + "</div>"
    s += "</div>"
    return s


@app.route("/Voice", methods=['GET', 'POST'])
def Voice():
    e = datetime.datetime.now()
    voice = request.form["a"]
    f = open("/home/mustar/voice_records.txt", "a+")
    f.write("%s: %s\n" % (e, voice))
    f.close()
    print(voice)
    return "OK"


app.run("127.0.0.1", debug=True)