#!/usr/bin/python3
import glob
import os
import re
import json
import datetime
from textwrap import indent

GITHUB_REPOSITORY_URL = 'https://github.com/PAPAMICA/docker-compose-collection'
SERVICES="|:--:|--|--|--|--|"
SERVICES_TODO="|:--:|--|"
try:
    os.remove("./templates-portainer.json") 
    os.remove("./README.md") 
except:
    print ("file don't exist")
result = {}
result["version"] = "2"
result["templates"] = []
templates = []
nb_a = 0
nb_td = 0

for filename in sorted(glob.glob("composes-files/*.y*ml")):
    try:
        data = []
        dataset = {}
        repository = {}
        env = []
        categories = []
        file_name=filename.split('/')
        file_name=file_name[1]
        file_name=file_name[:-4]
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
                elif data[0] == "note":
                    try:
                        link = re.search("(?<=href=')[^']+(?=')", data[1]).group()
                        website = re.search("(?<=rel='noopener'>)[^']+(?=<\/a)", data[1]).group()
                    except:
                        link=""
                        website=""
                    dataset[data[0]] = data[1]
                    print(link)
                elif data[0] == "title":
                    title = data[1]
                    dataset[data[0]] = title
                    dataset["name"] = title
                elif data[0] == "logo":
                    logo = data[1]
                    dataset[data[0]] = logo
                else:
                    dataset[data[0]] = data[1]
            if re.search('# Update:', line):
                date=line[10:-1]
            if re.search('# Maintainer:', line):
                maintainer=line[13:-1]
            if re.search('#%', line):
                envtemp = {}
                dataenv=line[3:-1].split(': ', 1)
                envtemp["name"] = dataenv[0]
                try:
                    envdesctotal = re.split('\(|\[', dataenv[1])
                    envdesc = envdesctotal[1]
                    envhold = envdesctotal[2]
                    envtemp["label"] = envdesctotal[0]
                    envtemp["description"] = envdesc[:-2]
                    envtemp["default"] = envhold[:-1]
                except:
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
                "stackfile": filename,
                "url": GITHUB_REPOSITORY_URL,
            }
            dataset["repository"] = repository
            #dataset["type"] = 3
            dataset["env"] = env
            templates.append(dataset)
            print (f" ✅ {filename} ")
            SERVICES=SERVICES + f'\n| ✅ | <img src="{logo}" alt="{file_name}" width="20"/> [{file_name}](https://github.com/PAPAMICA/docker-compose-collection/tree/master/composes-files/{file_name}.yml) | [{website}]({link}) | {date} | {maintainer} |'
            nb_a += 1
            
        else:
            print (f" 🚸 {filename} not updated !")
            SERVICES_TODO=SERVICES_TODO + f"\n| 🚸 | {file_name} |"
            nb_td += 1
    except:
         print (f" ❌ {filename} error !")

try:
    result["templates"] = templates
    json_data = json.dumps(result, indent=4)
    with open('./templates-portainer.json', 'w') as outfile:
        outfile.write(json_data)
    print ("\n ✅ templates-portainer.json generated !")
    try:
        try:
            os.remove("./README.md") 
        except:
            print ("file don't exist")
        DATE = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%M")
        nb_a = f'<img src="https://img.shields.io/badge/Availables:_{nb_a}-%2354B848.svg?style=for-the-badge&logo=cachet&logoColor=white">'
        nb_td = f'<img src="https://img.shields.io/badge/To_do:_{nb_td}-%23FF8800.svg?style=for-the-badge&logo=vlcmediaplayer&logoColor=white">'
        readme_template = open(".github/workflows/Readme-template.md", "rt")
        readme_result = open("README.md", "wt")
        for line in readme_template:
            readme_result.write(line.replace('##DATE##', DATE).replace('##SERVICES##', SERVICES).replace('##SERVICES_TODO##', SERVICES_TODO).replace('##NB_A##', nb_a).replace('##NB_TD##', nb_td))
        readme_template.close()
        readme_result.close()
        print ("\n ✅ README.md generated !")
    except:
        print (" ❌ Error when generate README.md !")

except:
    print (" ❌ Error when generate templates-portainer.json !")
