
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
| ✅ | adminer.yml | 2020-01-20 |
| ✅ | bookstack.yml | 2020-01-20 |
| ✅ | cachethq.yml | 2020-01-20 |
| ✅ | etherpad.yml | 2020-01-20 |
| ✅ | filebot.yml | 2020-01-20 |
| ✅ | filebrowser.yml | 2020-01-20 |
| 🚸 | gitlab.yml | 2020-01-20 |
| ✅ | grafana.yml | 2020-01-20 |
| ✅ | hastebin.yml | 2020-01-20 |
| ✅ | jirafeau.yml | 2020-01-20 |
| ✅ | keycloak.yml | 2020-01-20 |
| ✅ | matomo.yml | 2020-01-20 |
| 🚸 | nextcloud.yml | 2020-01-20 |
| 🚸 | openvpn.yml | 2020-01-20 |
| 🚸 | ouroboros.yml | 2020-01-20 |
| 🚸 | privatebin.yml | 2020-01-20 |
| 🚸 | projectsend.yml | 2020-01-20 |
| 🚸 | shorturl.yml | 2020-01-20 |
| 🚸 | sinusbot.yml | 2020-01-20 |
| 🚸 | taiga.yml | 2020-01-20 |
| 🚸 | teamspeak.yml | 2020-01-20 |
| 🚸 | traefik.yml | 2020-01-20 |
| 🚸 | ts3rank.yml | 2020-01-20 |
| 🚸 | ts3viewer.yml | 2020-01-20 |
| ✅ | umami.yml | 2020-01-20 |
| 🚸 | vault.yml | 2020-01-20 |
| ✅ | vaultwarden.yml | 2020-01-20 |
| 🚸 | vscode.yml | 2020-01-20 |
| ✅ | website-html.yml | 2020-01-20 |
| 🚸 | wikijs.yml | 2020-01-20 |
| 🚸 | wiznote.yml | 2020-01-20 |
| 🚸 | wordpress.yml | 2020-01-20 |
| 🚸 | yourls.yml | 2020-01-20 |
| 🚸 | zabbix-cachethq.yml | 2020-01-20 |
| 🚸 | zabbix-proxy.yml | 2020-01-20 |
| 🚸 | zabbix.yml | 2020-01-20 |


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
