
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
| ✅ | adminer.yml | 1652275689.104008 |
| ✅ | bookstack.yml | 1652275689.104008 |
| ✅ | cachethq.yml | 1652275689.104008 |
| ✅ | etherpad.yml | 1652275689.104008 |
| ✅ | filebot.yml | 1652275689.104008 |
| ✅ | filebrowser.yml | 1652275689.104008 |
| 🚸 | gitlab.yml | 1652275689.104008 |
| ✅ | grafana.yml | 1652275689.104008 |
| ✅ | hastebin.yml | 1652275689.104008 |
| ✅ | jirafeau.yml | 1652275689.104008 |
| ✅ | keycloak.yml | 1652275689.104008 |
| ✅ | matomo.yml | 1652275689.104008 |
| 🚸 | nextcloud.yml | 1652275689.104008 |
| 🚸 | openvpn.yml | 1652275689.104008 |
| 🚸 | ouroboros.yml | 1652275689.104008 |
| 🚸 | privatebin.yml | 1652275689.104008 |
| 🚸 | projectsend.yml | 1652275689.108008 |
| 🚸 | shorturl.yml | 1652275689.108008 |
| 🚸 | sinusbot.yml | 1652275689.108008 |
| 🚸 | taiga.yml | 1652275689.108008 |
| 🚸 | teamspeak.yml | 1652275689.108008 |
| 🚸 | traefik.yml | 1652275689.108008 |
| 🚸 | ts3rank.yml | 1652275689.108008 |
| 🚸 | ts3viewer.yml | 1652275689.108008 |
| ✅ | umami.yml | 1652275689.108008 |
| 🚸 | vault.yml | 1652275689.108008 |
| ✅ | vaultwarden.yml | 1652275689.108008 |
| 🚸 | vscode.yml | 1652275689.108008 |
| ✅ | website-html.yml | 1652275689.108008 |
| 🚸 | wikijs.yml | 1652275689.108008 |
| 🚸 | wiznote.yml | 1652275689.108008 |
| 🚸 | wordpress.yml | 1652275689.108008 |
| 🚸 | yourls.yml | 1652275689.108008 |
| 🚸 | zabbix-cachethq.yml | 1652275689.108008 |
| 🚸 | zabbix-proxy.yml | 1652275689.108008 |
| 🚸 | zabbix.yml | 1652275689.108008 |


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
