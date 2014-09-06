#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
count = 0
 
def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout
 
while True:
    print int(round(readadc(0)/10.24))
    time.sleep(0.2)
    """
    tmp1 = int(round(readadc(0)/10.24))
    print "in1:",tmp1
    count = count +1
    time.sleep(0.2)
    #print count
    """