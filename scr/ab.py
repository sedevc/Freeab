#!/usr/bin/env python
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')
import sqlite3, os, glob, time, threading
from colorama import Fore, Back, Style
import RPi.GPIO as GPIO

MAX_POWER_PROGRAM_MIN_TEMP = 200
IDLE_PROGRAM_MIN_TEMP = 70


GPIO_SCREW = 17 #OUT
GPIO_FAN = 18 #OUT
GPIO_MODE = 23 #IN
GPIO_MAN_SCREW = 24 #IN
GPIO_MAN_FAN = 25 #IN
FILE_NAME_LOG = 'log.txt'
FILE_NAME_BOILER = 'bTemp.txt'
FILE_NAME_FIRE = 'fTemp.txt'
FILE_NAME_TIMER = 'tempTimer.txt'
SENSOR_BASE_DIR = '/sys/bus/w1/devices/'
NUMBER_OF_SENSORS = 2
NUMBER_OF_FIRE_SENSORS = 1
DB_NAME = 'data.db'

def wLog(content):
    if os.path.isfile(FILE_NAME_LOG) == False:
        print content
        file = open(FILE_NAME_LOG, "w")
        file.write(time.ctime(time.time()) + " - F.TEMP: [" + str(f) + "] - B.TEMP: [" + str(b) + "]---->  " + content + "\n")
        file.close()
    else:
        print content
        file = open(FILE_NAME_LOG, "a")
        file.write(time.ctime(time.time()) + " - F.TEMP: [" + str(f) + "] - B.TEMP: [" + str(b) + "]---->  " + content + "\n")
        file.close()

def wInitLog(content):
    if os.path.isfile(FILE_NAME_LOG) == False:
        print content
        file = open(FILE_NAME_LOG, "w")
        file.write(time.ctime(time.time()) + " - F.TEMP: [x.xx] - B.TEMP: [x.xx]---->  " + content + "\n")
        file.close()
    else:
        print content
        file = open(FILE_NAME_LOG, "a")
        file.write(time.ctime(time.time()) + " - F.TEMP: [x.xx] - B.TEMP: [x.xx]---->  " + content + "\n")
        file.close()

   
def initTempSensors(NUMBER_OF_SENSORS, BASE_DIR):
    wInitLog("Initiate temp sensors.....")
    
    tempSensor = []
    if len(glob.glob(BASE_DIR + '28*')) < NUMBER_OF_SENSORS:
        wInitLog("  Find %d sensors. Expected %d .\n .....Quit " % (len(glob.glob(BASE_DIR + '28*')), NUMBER_OF_SENSORS))
        quit()
    for i in range(len(glob.glob(BASE_DIR + '28*'))):
        tempSensor.append(glob.glob(BASE_DIR + '28*')[i] + '/w1_slave')
        wInitLog("  " + tempSensor[i])
    wInitLog("Number of temp sensors: " + str(i+1))
    return tempSensor

def initFireTempSensors(NUMBER_OF_FIRE_SENSORS, BASE_DIR):
    wInitLog("Initiate fire temp sensors.....")
    
    fireTempSensor = []
    if len(glob.glob(BASE_DIR + '3b*')) < NUMBER_OF_FIRE_SENSORS:
        wInitLog("  Find %d sensors. Expected %d .\n .....Quit " % (len(glob.glob(BASE_DIR + '28*')), NUMBER_OF_SENSORS))
        quit()
    for i in range(len(glob.glob(BASE_DIR + '3b*'))):
        fireTempSensor.append(glob.glob(BASE_DIR + '3b*')[i] + '/w1_slave')
        wInitLog("  " + fireTempSensor[i])
    wInitLog("Number of fire temp sensors: " + str(i+1))
    return fireTempSensor

def read_temp(sensor):
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

class myThread (threading.Thread):
    def __init__(self, threadID, name, fanTime, screwTime, blockTime, FILE_NAME_TIMER):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.fanTime = fanTime
        self.screwTime = screwTime
        self.blockTime = blockTime
        self.FILE_NAME_TIMER = FILE_NAME_TIMER
    def run(self):
        wLog("Starting " + self.name)
        start_fan(self.fanTime, self.screwTime, self.blockTime, self.FILE_NAME_TIMER)
        wLog("Exiting " + self.name)

def start_fan(fanTime, screwTime, blockTime, FILE_NAME_TIMER):
    wLog("Start fan in %d secounds" % fanTime)
    wLog("Start screw in %d secounds" % screwTime)
    wLog("Block time set to %d secounds" % blockTime)
    if screwTime != 0:
        GPIO.output(GPIO_SCREW, True)
        wLog("Start screw")
    if fanTime != 0:
        GPIO.output(GPIO_FAN, True)
        wLog("Start fan")
    for i in xrange(blockTime,0,-1):
        if (blockTime-screwTime) == i and screwTime != 0:
            GPIO.output(GPIO_SCREW, False)
            wLog("Stop screw")
        if (blockTime-fanTime) == i and fanTime != 0:
            GPIO.output(GPIO_FAN, False)
            wLog("Stop fan")
        wFile(i, FILE_NAME_TIMER)
        #blockTimeLeft = i
        time.sleep(1)

def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_MODE, GPIO.IN)
    GPIO.setup(GPIO_MAN_SCREW, GPIO.IN)
    GPIO.setup(GPIO_MAN_FAN, GPIO.IN)

    GPIO.setup(GPIO_SCREW, GPIO.OUT)
    GPIO.setup(GPIO_FAN, GPIO.OUT)
    GPIO.output(GPIO_SCREW, False)
    GPIO.output(GPIO_FAN, False)
    wLog("GPIO Version: " + str(GPIO.VERSION))

def openDB(DB_NAME):

    if os.path.isfile(DB_NAME):
        try:
            global cur, con
            con = sqlite3.connect('data.db')
            cur = con.cursor()    
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            wLog("Open Database..... \n  SQLite version: %s \n  Database %s exist." % (data, DB_NAME))
        except sqlite3.Error, e:
            wLog("Error %s:" % e.args[0])
            quit()
    else:
        wLog("Database %s dosn't exist.....Create databse %s " % (DB_NAME, DB_NAME))
        quit()
 

    
def add_temp_db (zonestr, temp):
    cur.execute("""INSERT INTO temps values(date('now'),
        time('now'), (?), (?))""", (zonestr,temp))
    con.commit() # commit the changes



def wFile(content, tempfile):
    file = open(tempfile, "w")
    file.write(str(content))
    file.close()

def readFile(x):
    f = open(x, 'r')
    return f.read()

wInitLog("\n\n\n\n\n\n\n\n")
tempSensor = initTempSensors(NUMBER_OF_SENSORS, SENSOR_BASE_DIR)
fireTempSensor = initFireTempSensors(NUMBER_OF_FIRE_SENSORS, SENSOR_BASE_DIR)
t = read_temp(tempSensor[0])
b = read_temp(tempSensor[1])
f = read_temp(fireTempSensor[0])

startupSeq = myThread(1, "Fan-Thread", 0, 0, 0, FILE_NAME_TIMER)
maxpSeq = myThread(2, "MaxPower-Thread", 0, 0, 0, FILE_NAME_TIMER)
idleSeq = myThread(3, "Idle-Thread", 0, 0, 0, FILE_NAME_TIMER)
startupSeq.start()
maxpSeq.start()
idleSeq.start()




initGPIO()
openDB(DB_NAME)
time.sleep(0.5)
os.system('clear')
#af.initSim(FILE_NAME_BOILER, FILE_NAME_FIRE)
while True:
    while GPIO.input(GPIO_MODE):
        #time.sleep(1)
        
        t = read_temp(tempSensor[0])
        b = read_temp(tempSensor[1])
        f = read_temp(fireTempSensor[0])
        os.system('clear')
        #print "\033[37m\033[41mFire Temp: " + str(f) + "\033[0m" + "\033[94mBoiler Temp: " + str(b) + "\033[0m"
        
        print("FIRE.TEMP: " + Style.BRIGHT + Fore.RED + str(f) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
        print("BOIL.TEMP: " + Style.BRIGHT + Fore.BLUE + str(b) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
        print("TANK.TEMP: " + Style.BRIGHT + Fore.CYAN + str(t) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
        #print "F.TEMP: " + str(f)
        #print "B.TEMP: " + str(b)
        #print "T.TEMP: " + str(t)
        if GPIO.input(GPIO_SCREW) == True:
            print "Screw running"
        if GPIO.input(GPIO_FAN) == True:
            print "Fan running"

        if b <= 50:
            print "STARTUP PROGRAM"
            
            if GPIO.input(GPIO_FAN) == False:
                GPIO.output(GPIO_FAN, True)
            if startupSeq.isAlive() or maxpSeq.isAlive() or idleSeq.isAlive():
                print "Time left of blocktimer: " + str(readFile(FILE_NAME_TIMER))
            if startupSeq.isAlive() == False and maxpSeq.isAlive() == False and idleSeq.isAlive() == False:
                if f < 200:
                    startupSeq = myThread(1, "startUp-Thread", 0, 5, 60, FILE_NAME_TIMER)
                    startupSeq.start()
        elif b >= 51 and b <= 69:
            print "MAX POWER PROGRAM"
            if GPIO.input(GPIO_FAN) == False:
                GPIO.output(GPIO_FAN, True)
            
            if startupSeq.isAlive() or maxpSeq.isAlive() or idleSeq.isAlive() == True:
                print "Time left of blocktimer: " + str(readFile(FILE_NAME_TIMER))
            if f < MAX_POWER_PROGRAM_MIN_TEMP:
                if startupSeq.isAlive() == False and maxpSeq.isAlive() == False and idleSeq.isAlive() == False:
                    maxpSeq = myThread(2, "MaxPower-Thread", 0, 5, 60, FILE_NAME_TIMER)
                    maxpSeq.start()

        elif b >= 70 and b <= 99:
            print "IDLE PROGRAM"
            #if GPIO.input(GPIO_FAN) == True:
            #    GPIO.output(GPIO_FAN, False)
            if startupSeq.isAlive() or maxpSeq.isAlive() or idleSeq.isAlive() == True:
                print "Time left of blocktimer: " + str(readFile(FILE_NAME_TIMER))
            if f < IDLE_PROGRAM_MIN_TEMP:
                if startupSeq.isAlive() == False and maxpSeq.isAlive() == False and idleSeq.isAlive() == False:
                    idleSeq = myThread(3, "Idle-Thread", 20, 5, 60, FILE_NAME_TIMER)
                    idleSeq.start()
        print "\n\n\n"
        print time.ctime(time.time())   
    t = read_temp(tempSensor[0])
    b = read_temp(tempSensor[1])
    f = read_temp(fireTempSensor[0])
    os.system('clear')
    print("FIRE.TEMP: " + Style.BRIGHT + Fore.RED + str(f) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
    print("BOIL.TEMP: " + Style.BRIGHT + Fore.BLUE + str(b) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
    print("TANK.TEMP: " + Style.BRIGHT + Fore.CYAN + str(t) + Fore.RESET + Back.RESET + Style.RESET_ALL) 
    while GPIO.input(GPIO_MAN_SCREW):
        GPIO.output(GPIO_SCREW, True)
        wLog("Manuell run Screw")
        time.sleep(1)
    while GPIO.input(GPIO_MAN_FAN):
        GPIO.output(GPIO_FAN, True)
        wLog("Manuell run fan")
        time.sleep(1)
    print "Ready to go...."
    time.sleep(0.3)
    GPIO.output(GPIO_SCREW, False)
    GPIO.output(GPIO_FAN, False)
    #os.system('clear')
con.close()
print(Fore.RESET + Back.RESET + Style.RESET_ALL)


