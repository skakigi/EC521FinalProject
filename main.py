"""
    Main executable File : Coupled with bash script, reads in vulnerabilities scanned

"""

import json

d = "vulnapi_scripts/"

output_file = d + "results.json"

type_file = d + "type.txt"
url_file = d + "url.txt"
high_file = d + "high.txt"
medium_file = d + "medium.txt"
low_file = d + "low.txt"
info_file = d + "info.txt"



def isEmpty(file):
    with open(file,"r") as file_obj:
        if file_obj.read(1):
            return True
        else:
            return False

def writeData(data):

    with open(output_file, "w") as out_file:
        json.dump(data, out_file,indent=4)

def readData(file):
    file_object = open(file, "r")
    return file_object.readlines()
"""
    ---------------------- Execution Start ----------------------
"""


high_exist = isEmpty(high_file)
medium_exist = isEmpty(medium_file)
low_exist = isEmpty(low_file)
info_exist = isEmpty(info_file)

if high_exist: high_data = readData(high_file)
else: high_data = []

if medium_exist:medium_data = readData(medium_file)
else: medium_data = []

if low_exist:low_data = readData(low_file)
else: low_data = []

if info_exist:info_data = readData(info_file)
else: info_data = []

url_data = readData(url_file)
type_data = readData(type_file)

data={
    url_data[0]:{
        "Type":type_data,
        "High": high_data,
        "Medium": medium_data,
        "Low": low_data,
        "Info": info_data
    }
}

with open(output_file, "r") as file:
    curr = json.load(file)
with open("vulnapi_scripts/results.json",'a') as file:
    if not url_data[0] in curr:
        writeData(data)


