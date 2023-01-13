#!/usr/bin/env python3
import sys, logging, jinja2
from datetime import date

#logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
#logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def volumlist():
    volumlist = []
    volume_name = "Nothing" 
    while volume_name != "":
        volume_name = input("Enter volume name or press enter to exit : ")
        if volume_name != "":
            volume_dir = input("Enter the directory mounted inside the container : ")
            volumlist.append(f"{volume_name}:{volume_dir}")
    print(volumlist)
    return volumlist

def envvar():
    envvar = []
    var_name = "Nothing" 
    while var_name != "":
        var_name = input("Enter environment variable or press enter to exit : ")
        if var_name != "":
            grp_var =  []
            var_description = input(f"  Enter description of variable {var_name} : ")
            var_hint = input(f"  Enter hint of variable {var_name} : ")
            var_default = input(f"  Enter default of variable {var_name} : ")
            grp_var.append(var_name)
            grp_var.append(var_description)
            grp_var.append(var_hint)
            grp_var.append(var_default)
            envvar.append(grp_var)
    print(envvar)
    return envvar

app_name            = input("App's name : ")
app_logo            = input("App's logo (url) : ")
app_image           = input("App's Docker image : ")
app_port            = input("App's port : ")
app_url             = input("App's official github repo : ")
app_description     = input("App's description : ")
maintainer_name     = input("Maintainer's name : ")
maintainer_github   = input("Maintainer's github profile : ")
#app_name            = "Ampache"
#app_logo            = "https://ampache.org/img/logo/ampache-logo.png"
#app_image           = "ampache/ampache:latest"
#app_port            = "80"
#app_url             = "https://github.com/ampache/ampache-docker"
#app_description     = "web based audio/video streaming application and file manager allowing you to access your music & videos from anywhere, using almost any internet enabled device."
#maintainer_name     = "Quentin JOLY"
#maintainer_github   = "@QJoly"
envvar              = envvar()
volumlist           = volumlist()

data = {
        'app_name'           : app_name,
        'app_logo'           : app_logo,
        'app_image'          : app_image,
        'app_port'           : app_port,
        'app_url'            : app_url,
        'app_description'    : app_description,
        'maintainer_name'    : maintainer_name,
        'maintainer_github'  : maintainer_github,
        'envvar'             : envvar,
        'volumlist'          : volumlist,
        'update_date'        : date.today().strftime("%Y-%m-%d")
        }

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.yml.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(data)  

output = open(f"./{app_name}.yml".lower(), "w")
output.write(outputText)
output.close()
 
