
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
| ✅ | adminer.yml | 2022-05-11 13:30:23.679861 |
| ✅ | bookstack.yml | 2022-05-11 13:30:23.679861 |
| ✅ | cachethq.yml | 2022-05-11 13:30:23.679861 |
| ✅ | etherpad.yml | 2022-05-11 13:30:23.683861 |
| ✅ | filebot.yml | 2022-05-11 13:30:23.683861 |
| ✅ | filebrowser.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | gitlab.yml | 2022-05-11 13:30:23.683861 |
| ✅ | grafana.yml | 2022-05-11 13:30:23.683861 |
| ✅ | hastebin.yml | 2022-05-11 13:30:23.683861 |
| ✅ | jirafeau.yml | 2022-05-11 13:30:23.683861 |
| ✅ | keycloak.yml | 2022-05-11 13:30:23.683861 |
| ✅ | matomo.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | nextcloud.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | openvpn.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | ouroboros.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | privatebin.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | projectsend.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | shorturl.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | sinusbot.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | taiga.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | teamspeak.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | traefik.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | ts3rank.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | ts3viewer.yml | 2022-05-11 13:30:23.683861 |
| ✅ | umami.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | vault.yml | 2022-05-11 13:30:23.683861 |
| ✅ | vaultwarden.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | vscode.yml | 2022-05-11 13:30:23.683861 |
| ✅ | website-html.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | wikijs.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | wiznote.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | wordpress.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | yourls.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | zabbix-cachethq.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | zabbix-proxy.yml | 2022-05-11 13:30:23.683861 |
| 🚸 | zabbix.yml | 2022-05-11 13:30:23.683861 |


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
