#!/usr/bin/python3
import glob
import os
import re
import json
from textwrap import indent

GITHUB_REPOSITORY_URL = 'https://github.com/PAPAMICA/docker-compose-collection'
try:
    os.remove("./templates-portainer.json") 
except:
    print ("file don't exist")
result = {}
result["version"] = "2"
result["templates"] = []
templates = []

for filename in glob.glob("*.y*ml"):
    data = []
    dataset = {}
    repository = {}
    env = []
    categories = []
    file = open(filename)
    for line in file.readlines():
        if re.search('#&', line):
            data=line[3:-1].split(': ', 1)
            if data[0] == "categories":
                categories = data[1].split(', ')
                dataset[data[0]] = categories
            if data[0] == "note":
                note = data[1].translate(str.maketrans({"-":  r"\-",
                                                        "]":  r"\]",
                                                        "^":  r"\^",
                                                        "$":  r"\$",
                                                        "*":  r"\*"}))
                dataset[data[0]] = note
            else:
                dataset[data[0]] = data[1]
        if re.search('#%', line):
            envtemp = {}
            dataenv=line[3:-1].split(': ', 1)
            envtemp["name"] = dataenv[0]
            envtemp["label"] = dataenv[1]
            env.append(envtemp)
    if data:
        repository = {
            "url": GITHUB_REPOSITORY_URL,
            "stackfile": filename
        }
        dataset["repository"] = repository
        dataset["env"] = env
        templates.append(dataset)
        
    #else:
        #print (f"{filename} not updated !")

result["templates"] = templates
json_data = json.dumps(result, indent=4)
with open('templates-portainer.json', 'w') as outfile:
    outfile.write(json_data)