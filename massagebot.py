#!/usr/bin/env python3

import threading
import rtde_control
from os import path
from os import path

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

speed_factor = 0.66
force_factor = 0.66
state = False
do_traps = True
do_lats = True
do_erector = True

max_force = 30
max_speed = 1

c7_xyz = [-0.345, 0.262, 0.360, 0, 0, 0]

task_frame = [0, 0, 0, 0, 0, 0]
selection_vector = [1, 0, 0, 0, 0, 0]
wrench = [1, 0, 0, 0, 0, 0]  # Set force here
force_type = 2
limits = [1, 0, 0, 0, 0, 0]  # Set Speed Here

traps = []
traps.append([0.025, 0.050])
traps.append([0.025, 0.075])
traps.append([0.050, 0.050])
traps.append([0.075, 0.050])
traps.append([0.100, 0.050])
traps.append([0.125, 0.050])
traps.append([0.150, 0.050])
traps.append([0.175, 0.050])
traps.append([0.200, 0.050])

lats = []
lats.append([0.225, 0.050])
lats.append([0.250, 0.050])
lats.append([0.275, 0.050])
lats.append([0.300, 0.050])

erects_tehe = []
erects_tehe.append([0.325, 0.050])
erects_tehe.append([0.350, 0.050])
erects_tehe.append([0.375, 0.050])
erects_tehe.append([0.400, 0.050])

def updateSettings():
    global speed_factor, force_factor, state, do_traps, do_lats, do_erector

    if path.exists("massageSettings.yaml"):
        try:
            inFile = open("massageSettings.yaml", 'r')
            data = load(inFile, Loader=Loader)
            inFile.close()

            do_erector = data["do_erector"]
            do_lats = data["do_lats"]
            do_traps = data["do_traps"]
            force_factor = data["force_factor"]
            speed_factor = data["speed_factor"]
            state = data["state"]
        except:
            pass

def makeMove(rtde_c, point):
    pose = rtde_c.poseTrans(c7_xyz, [point[0], 0.0, point[1], 4.712, 0.0, 0.0])
    rtde_c.moveL(pose, max_speed * speed_factor, 0.2)

def main():

    print("Starting Control...")
    rtde_c = rtde_control.RTDEControlInterface("192.168.2.66")
    rtde_c.setTcp([0.0, 0.0, 0.05, 0.0, 0.0, 0.0])

    while(True):
        rtde_c.moveJ([-1.5707, -2.26893, 2.26893, -3.22886, -1.48352986, 0])

        for p in traps:
            updateSettings()
            if do_traps and state:
                makeMove(rtde_c, p)
            else:
                break
        for p in lats:
            updateSettings()
            if do_lats and state:
                makeMove(rtde_c, p)
            else:
                break
        for p in erects_tehe:
            updateSettings()
            if do_erector and state:
                makeMove(rtde_c, p)
            else:
                break

    print("Done")
    #rtde_c.forceMode(task_frame, selection_vector, wrench, force_type, limits)

    #rtde_c.forceModeStop()

main()
