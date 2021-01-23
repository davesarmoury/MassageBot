#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask_cors import CORS
from distutils import util

from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/settings")
def updateSettings():
    data = {}

    data["speed_factor"] = float(request.args.get("speed"))
    data["force_factor"] = float(request.args.get("force"))
    data["state"] = bool(util.strtobool(request.args.get("state")))
    data["do_traps"] = bool(util.strtobool(request.args.get("upper")))
    data["do_lats"] = bool(util.strtobool(request.args.get("mid")))
    data["do_erector"] = bool(util.strtobool(request.args.get("lower")))

    outFile = open("massageSettings.yaml", 'w')
    outFile.write(dump(data, Dumper=Dumper))
    outFile.close()

    line = "Received <" + str(data["speed_factor"]) + ", " + str(data["force_factor"]) + ", " + str(data["state"]) + ", " + str(data["do_traps"]) + ", " + str(data["do_lats"]) + ", " + str(data["do_erector"]) + ">"
    print(line)
    return line

def main():
    app.run("0.0.0.0")

main()
