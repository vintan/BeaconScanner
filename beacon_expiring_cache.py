# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

from expiringdict import ExpiringDict

import bluetooth._bluetooth as bluez

cache = ExpiringDict(max_len=100, max_age_seconds=30)

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "beacon scanning thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
        for keys,values in cache.items():
            print "cache item"
            print(keys)
            print(values)
	print "----------"
	for beacon in returnedList:
                details = beacon.split(',')
                #if details[2] == "4660" and details[3] == "17185":
                    #print details[1]
                    #cache[details[1]] = details[5]
                print details[1]
                cache[details[1]] = details[5]
                    #print beacon


