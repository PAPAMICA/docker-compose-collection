
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
| ✅ | adminer.yml | 10/05/2022
 |
| ✅ | bookstack.yml | 10/05/2022
 |
| ✅ | cachethq.yml | 10/05/2022
 |
| ✅ | etherpad.yml | 10/05/2022
 |
| ✅ | filebot.yml | 10/05/2022
 |
| ✅ | filebrowser.yml | 10/05/2022
 |
| 🚸 | gitlab.yml |
| ✅ | grafana.yml | 10/05/2022
 |
| ✅ | hastebin.yml | 10/05/2022
 |
| ✅ | jirafeau.yml | 10/05/2022
 |
| ✅ | keycloak.yml | 10/05/2022
 |
| ✅ | matomo.yml | 10/05/2022
 |
| 🚸 | nextcloud.yml |
| 🚸 | openvpn.yml |
| 🚸 | ouroboros.yml |
| 🚸 | privatebin.yml |
| 🚸 | projectsend.yml |
| 🚸 | shorturl.yml |
| 🚸 | sinusbot.yml |
| 🚸 | taiga.yml |
| 🚸 | teamspeak.yml |
| 🚸 | traefik.yml |
| 🚸 | ts3rank.yml |
| 🚸 | ts3viewer.yml |
| ✅ | umami.yml | 10/05/2022
 |
| 🚸 | vault.yml |
| ✅ | vaultwarden.yml | 10/05/2022
 |
| 🚸 | vscode.yml |
| ✅ | website-html.yml | 10/05/2022
 |
| 🚸 | wikijs.yml |
| 🚸 | wiznote.yml |
| 🚸 | wordpress.yml |
| 🚸 | yourls.yml |
| 🚸 | zabbix-cachethq.yml |
| 🚸 | zabbix-proxy.yml |
| 🚸 | zabbix.yml |


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
