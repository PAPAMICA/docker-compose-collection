
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
| ✅ | adminer.yml | 11-05-22 13:32:53 |
| ✅ | bookstack.yml | 11-05-22 13:32:53 |
| ✅ | cachethq.yml | 11-05-22 13:32:53 |
| ✅ | etherpad.yml | 11-05-22 13:32:53 |
| ✅ | filebot.yml | 11-05-22 13:32:53 |
| ✅ | filebrowser.yml | 11-05-22 13:32:53 |
| 🚸 | gitlab.yml | 11-05-22 13:32:53 |
| ✅ | grafana.yml | 11-05-22 13:32:53 |
| ✅ | hastebin.yml | 11-05-22 13:32:53 |
| ✅ | jirafeau.yml | 11-05-22 13:32:53 |
| ✅ | keycloak.yml | 11-05-22 13:32:53 |
| ✅ | matomo.yml | 11-05-22 13:32:53 |
| 🚸 | nextcloud.yml | 11-05-22 13:32:53 |
| 🚸 | openvpn.yml | 11-05-22 13:32:53 |
| 🚸 | ouroboros.yml | 11-05-22 13:32:53 |
| 🚸 | privatebin.yml | 11-05-22 13:32:53 |
| 🚸 | projectsend.yml | 11-05-22 13:32:53 |
| 🚸 | shorturl.yml | 11-05-22 13:32:53 |
| 🚸 | sinusbot.yml | 11-05-22 13:32:53 |
| 🚸 | taiga.yml | 11-05-22 13:32:53 |
| 🚸 | teamspeak.yml | 11-05-22 13:32:53 |
| 🚸 | traefik.yml | 11-05-22 13:32:53 |
| 🚸 | ts3rank.yml | 11-05-22 13:32:53 |
| 🚸 | ts3viewer.yml | 11-05-22 13:32:53 |
| ✅ | umami.yml | 11-05-22 13:32:53 |
| 🚸 | vault.yml | 11-05-22 13:32:53 |
| ✅ | vaultwarden.yml | 11-05-22 13:32:53 |
| 🚸 | vscode.yml | 11-05-22 13:32:53 |
| ✅ | website-html.yml | 11-05-22 13:32:53 |
| 🚸 | wikijs.yml | 11-05-22 13:32:53 |
| 🚸 | wiznote.yml | 11-05-22 13:32:53 |
| 🚸 | wordpress.yml | 11-05-22 13:32:53 |
| 🚸 | yourls.yml | 11-05-22 13:32:53 |
| 🚸 | zabbix-cachethq.yml | 11-05-22 13:32:53 |
| 🚸 | zabbix-proxy.yml | 11-05-22 13:32:53 |
| 🚸 | zabbix.yml | 11-05-22 13:32:53 |


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
