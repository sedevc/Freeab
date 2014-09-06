import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'



device_folder1 = glob.glob(base_dir + '28*')[0]
device_folder2 = glob.glob(base_dir + '3b*')[0]

UTE = device_folder1 + '/w1_slave'
INNE = device_folder2 + '/w1_slave'
	


def read_temp_raw(sensor):
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(sensor):
    lines = read_temp_raw(sensor)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
	
while True:
	print('UTE TEMP : ' + str(read_temp(UTE)))	
	print('INNE TEMP: ' + str(read_temp(INNE)))	
	time.sleep(2)
