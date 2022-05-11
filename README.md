
# Docker-compose by PAPAMICA
|  ![PAPAMICA](https://zupimages.net/up/20/04/7vtd.png) |  [Wiki-Tech.io](https://Wiki-Tech.io/)<br/> [Tech2Tech.fr](https://www.tech2tech.fr/) <br/> [Twitter @PAPAMICA__](https://twitter.com/PAPAMICA__) <br/> [LinkedIn](https://www.linkedin.com/in/mickael-asseline/)<br/> |
|:--------:| :-------------|


These docker-compose allow you to deploy multiple services easily and quickly. You can use them with Portainer directly or via docker-compose commands.
All docker-compose are commented and are configured using variables.

They all include support for Traefik.

You can deploye a compatible Docker environment with Portainer and Traefik with :
https://github.com/PAPAMICA/docker-environment



## List of services availables:
| Status | Service | Update |
|:--:|--|--|
| ✅ | adminer.yml | prout |
| ✅ | bookstack.yml | prout |
| ✅ | cachethq.yml | prout |
| ✅ | etherpad.yml | prout |
| ✅ | filebot.yml | prout |
| ✅ | filebrowser.yml | prout |
| 🚸 | gitlab.yml | prout |
| ✅ | grafana.yml | prout |
| ✅ | hastebin.yml | prout |
| ✅ | jirafeau.yml | prout |
| ✅ | keycloak.yml | prout |
| ✅ | matomo.yml | prout |
| 🚸 | nextcloud.yml | prout |
| 🚸 | openvpn.yml | prout |
| 🚸 | ouroboros.yml | prout |
| 🚸 | privatebin.yml | prout |
| 🚸 | projectsend.yml | prout |
| 🚸 | shorturl.yml | prout |
| 🚸 | sinusbot.yml | prout |
| 🚸 | taiga.yml | prout |
| 🚸 | teamspeak.yml | prout |
| 🚸 | traefik.yml | prout |
| 🚸 | ts3rank.yml | prout |
| 🚸 | ts3viewer.yml | prout |
| ✅ | umami.yml | prout |
| 🚸 | vault.yml | prout |
| ✅ | vaultwarden.yml | prout |
| 🚸 | vscode.yml | prout |
| ✅ | website-html.yml | prout |
| 🚸 | wikijs.yml | prout |
| 🚸 | wiznote.yml | prout |
| 🚸 | wordpress.yml | prout |
| 🚸 | yourls.yml | prout |
| 🚸 | zabbix-cachethq.yml | prout |
| 🚸 | zabbix-proxy.yml | prout |
| 🚸 | zabbix.yml | prout |


# Utilisation
## Portainer
Add the URL of my repo directly in Portainer:
![PORTAINER](https://i.imgur.com/M49ssCN.png)

## Debian
Install Git :
```bash
 apt install -y git
```

Clone repo
```bash
git clone https://github.com/PAPAMICA/docker-compose-collection/
```


Configuration of variables and execution of a docker-compose:
```bash
cd docker-compose-collection
nano env
sudo docker-compose -f service.yml --env-file env up -d
```
## Some useful commands:

-   **docker container ls** : Show current Docker containers
-   **docker-compose stop** : Stop the containers created with the scripts (in the script folder)
- **docker-compose up -d** : Launch the containers created with the scripts (in the script folder)
-   **docker logs -f <id_container>** : Display the container logs
-   **docker exec -it <id_container> bash** : Get a shell in container
