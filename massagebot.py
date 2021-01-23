#!/usr/bin/env python3

from flask import Flask
from flask import request
import threading
import rtde_control
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

speed_factor = 0.66
force_factor = 0.66
state = 0

max_force = 30
max_speed = 1

c7_xyz = [0, 0, 0, 0, 0, 1.5707]

task_frame = [0, 0, 0, 0, 0, 0]
selection_vector = [0, 0, 1, 0, 0, 0]
wrench = [0, 0, 1, 0, 0, 0]  # Set force here
force_type = 2
limits = [0, 0, 1, 0, 0, 0]  # Set Speed Here

do_traps = True
do_lats = True
do_etector = True

traps = []
traps.append([-1, 2])
traps.append([-1, 3])
traps.append([-2, 2])
traps.append([-3, 2])
traps.append([-4, 2])
traps.append([-5, 2])
traps.append([-6, 2])
traps.append([-7, 2])
traps.append([-8, 2])

lats = []
lats.append([-9, 2])
lats.append([-10, 2])
lats.append([-11, 2])
lats.append([-12, 2])

erects_tehe = []
erects_tehe.append([-13, 2])
erects_tehe.append([-14, 2])
erects_tehe.append([-15, 2])
erects_tehe.append([-16, 2])

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/settings")
def updateSettings():
    global speed_factor, force_factor, state
    speed_factor = request.args.get("speed")
    force_factor = request.args.get("force")
    state = request.args.get("state")
    do_traps = request.args.get("upper")
    do_lats = request.args.get("mid")
    do_etector = request.args.get("lower")

    print("Received <" + str(speed_factor) + ", " + str(force_factor) + ", " + str(state) + ", " + str(do_traps) + ", " + str(do_lats) + ", " + str(do_etector) + ">")
    return "Received <" + str(speed_factor) + ", " + str(force_factor) + ", " + str(state) + ", " + str(do_traps) + ", " + str(do_lats) + ", " + str(do_etector) + ">"

def main():
    print("Starting web server...")
    threading.Thread(target=app.run("0.0.0.0")).start()

    #rtde_c = rtde_control.RTDEControlInterface("192.168.2.66")
    #rtde_c.forceMode(task_frame, selection_vector, wrench, force_type, limits)
    #rtde_c.moveL([-0.143, -0.435, 0.20, -0.001, 3.12, 0.04], 0.5, 0.3)
    #rtde_c.forceModeStop()

main()
