import time
import RPi.GPIO as GPIO

TIME = 3
FILE_NAME_BOILER = 'bTemp.txt'
START_VALUE = 25
MIN_VALUE = 56
MAX_VALUE = 99

def wFile(stat):
	file = open(FILE_NAME_BOILER, "w")
	file.write(str(stat))
	file.close()

 


for i in range(START_VALUE, MIN_VALUE, 1):
    time.sleep(TIME)
    print(i)
    wFile(i)
 	

while True:
	for i in range(MIN_VALUE, MAX_VALUE, 1):
    		time.sleep(TIME)
    		print(i)
 		wFile(i)

	for i in range(MAX_VALUE, MIN_VALUE, -1):
    		time.sleep(TIME)
    		print(i)
 		wFile(i)



