import time

TIME = 1
FILE_NAME_FIRE = 'fTemp.txt'
START_VALUE = 0
MIN_VALUE = 200
MAX_VALUE = 850

def wFile(stat):
	file = open(FILE_NAME_FIRE, "w")
	file.write(str(stat))
	file.close()

for i in range(START_VALUE, MIN_VALUE, 3):
    time.sleep(TIME)
    print(i)
    wFile(i)
 	

while True:
	for i in range(MIN_VALUE, MAX_VALUE, 2):
    		time.sleep(TIME)
    		print(i)
 		wFile(i)

	for i in range(MAX_VALUE, MIN_VALUE, -2):
    		time.sleep(TIME)
    		print(i)
 		wFile(i)



