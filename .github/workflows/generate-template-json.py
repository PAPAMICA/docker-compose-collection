#!/usr/bin/python3
import glob
import os
import re
import json
from textwrap import indent

GITHUB_REPOSITORY_URL = 'https://github.com/PAPAMICA/docker-compose-collection/composes-files'
SERVICES="|:--:|--|--|"
try:
    os.remove("./templates-portainer.json") 
except:
    print ("file don't exist")
result = {}
result["version"] = "2"
result["templates"] = []
templates = []

for filename in sorted(glob.glob("composes-files/*.y*ml")):
    try:
        data = []
        dataset = {}
        repository = {}
        env = []
        categories = []
        file_name=filename.split('/')
        file_name=file_name[1]
        file = open(filename)
        for line in file.readlines():
            if re.search('#&', line):
                data=line[3:-1].split(': ', 1)
                if data[0] == "type":
                    type_=int(data[1])
                    dataset[data[0]] = type_
                elif data[0] == "categories":
                    categories = data[1].split(', ')
                    dataset[data[0]] = categories
                elif data[0] == "title":
                    title = data[1]
                    dataset[data[0]] = title
                else:
                    dataset[data[0]] = data[1]
            if re.search('#%', line):
                envtemp = {}
                dataenv=line[3:-1].split(': ', 1)
                envtemp["name"] = dataenv[0]
                try:
                    envdesctotal = dataenv[1].split(' (')
                    envdesc = envdesctotal[1]
                    envtemp["label"] = envdesctotal[0]
                    envtemp["description"] = envdesc[:-1]
                except:
                    envtemp["label"] = dataenv[1]
                env.append(envtemp)
        if data:
            repository = {
                "url": GITHUB_REPOSITORY_URL,
                "stackfile": filename
            }
            dataset["repository"] = repository
            #dataset["type"] = 3
            dataset["env"] = env
            templates.append(dataset)
            print (f" ✅ {filename} ")
            SERVICES=SERVICES + f"\n| ✅ | {file_name} | 2020-01-20 |"
            
        else:
            print (f" 🚸 {filename} not updated !")
            SERVICES=SERVICES + f"\n| 🚸 | {file_name} | 2020-01-20 |"
    except:
         print (f" ❌ {filename} error !")

try:
    result["templates"] = templates
    json_data = json.dumps(result, indent=4)
    with open('./templates-portainer.json', 'w') as outfile:
        outfile.write(json_data)
    print ("\n ✅ File generated !")
    print (SERVICES)
except:
    print (" ❌ Error when generate !")