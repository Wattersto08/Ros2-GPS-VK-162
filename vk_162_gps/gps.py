#!/usr/bin/env python3
# Original Code: https://gist.github.com/Lauszus/5785023#file-gps-py
# Created by: Kristian Sloth Lauszus

import time
import serial

def readString():
    while 1:
        while ser.read().decode("utf-8") != '$':  # Wait for the begging of the string
            pass  # Do nothing
        line = ser.readline().decode("utf-8")  # Read the entire string
        return line


def getTime(string, format, returnFormat):
    return time.strftime(returnFormat,
                         time.strptime(string, format))  # Convert date and time to a nice printable format


def getLatLng(latString, lngString):
    lat = latString[:2].lstrip('0') + "." + "%.7s" % str(float(latString[2:]) * 1.0 / 60.0).lstrip("0.")
    lng = lngString[:3].lstrip('0') + "." + "%.7s" % str(float(lngString[3:]) * 1.0 / 60.0).lstrip("0.")
    return lat, lng




def printLite(lines):
    latlng = getLatLng(lines[2], lines[4])
    latitude = float(latlng[0])
    longitude = float(latlng[1])
    altitude = float (lines[9])
    return latitude,longitude,altitude


def checksum(line):
    checkString = line.partition("*")
    checksum = 0
    for c in checkString[0]:
        checksum ^= ord(c)

    try:  # Just to make sure
        inputChecksum = int(checkString[2].rstrip(), 16);
    except:
        print("Error in string")
        return False

    if checksum == inputChecksum:
        return True
    else:
        print("=====================================================================================")
        print("===================================Checksum error!===================================")
        print("=====================================================================================")
        print(hex(checksum), "!=", hex(inputChecksum))
        return False


def getGPS(device):
    global ser 
    ser = serial.Serial(device, 9600, timeout=1)  # Open Serial port
    while True:
        line = readString()
        lines = line.split(",")
        if checksum(line):
            if lines[0] == "GPGGA":
                return printLite(lines)
        else:
            return 0.0, 0.0, 0.0      



if __name__ == '__main__':
    print(getGPS('/dev/ttyACM0'))

