import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import math
import urllib.request
import json
f = open("file.txt", "w+");
for i in range(1, 10):
    f.write("The single digit numbers are " + str(i) + "\r\n");

def printResults(data):
    theJSON = json.loads(data)
    if "latitude" and "longitude" in theJSON["iss_position"]:
        f.write("Latitude: " + str(theJSON["iss_position"]["latitude"]) + " Longitude: " + str(theJSON["iss_position"]["longitude"]))
    else:
        print("Cannot print results")    
print(os.name)
print("Path exists: " + str(path.exists("file.txt")))
print("Path is a file: " + str(path.isfile("file.txt")))
print("Path is a directory: " + str(path.isdir("file.txt")))
def main():
    urldata = "http://api.open-notify.org/iss-now.json"

    webUrl = urllib.request.urlopen(urldata)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
       data = webUrl.read().decode("utf-8")
       printResults(data)
    else:
        print("Error, cannot parse results")

if __name__ == "__main__":
    main()            
