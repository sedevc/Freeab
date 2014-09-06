import sqlite3, os, glob, time, threading
import RPi.GPIO as GPIO


FILE_NAME_LOG = 'log.txt'
FILE_NAME_BOILER = 'bTemp.txt'
FILE_NAME_FIRE = 'fTemp.txt'

GPIO_SCREW = 17 #IN
GPIO_FAN = 18 #IN
GPIO_MODE = 23 #OUT
GPIO_MAN_SCREW = 24 #OUT
GPIO_MAN_FAN = 25 #OUT  













def initSim(FILE_NAME_BOILER, FILE_NAME_FIRE):
    wLog("Initiate fire/boiler temp simulator....\n  Set bTemp[25C]\n  Set fTemp[25C]")
    file = open(FILE_NAME_BOILER, "w")
    file.write("25")
    file.close()
    file = open(FILE_NAME_FIRE, "w")
    file.write("25")
    file.close()

