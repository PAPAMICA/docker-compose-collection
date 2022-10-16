#!/usr/bin/env python3
import sys, logging, jinja2

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def envvar():
    print("Enter environment variabble")
    envvar = []
    user_input = "Nothing" 
    while user_input != "":
        user_input = input("Enter environmnet variable or press enter to exit")
        if user_input != "":
            envvar.append(user_input)
    print(envvar)
    return envvar

envvar              = envvar()
maintainer_name     = "Demo_Name"
maintainer_github   = "@Demo"
app_name            = "Demo_Appname"
app_logo            = "demo_applogo"
app_image           = "demo_appimage"
app_port            = "8080"

data = {
        'app_name'           : app_name,
        'app_logo'           : app_logo,
        'app_image'          : app_image,
        'maintainer_name'    : maintainer_name,
        'maintainer_github'  : maintainer_github,
        'envvar'             : envvar
        }

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.yml.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(data)  

print(outputText)

