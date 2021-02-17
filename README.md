
# Docker-compose by PAPAMICA
|  ![PAPAMICA](https://zupimages.net/up/20/04/7vtd.png) |  [Labo-Tech.fr](https://labo-tech.fr/)<br/> [Tech2Tech.fr](https://www.tech2tech.fr/) <br/> [Twitter @PAPAMICA__](https://twitter.com/PAPAMICA__) <br/> [LinkedIn](https://www.linkedin.com/in/mickael-asseline/)<br/> |
|:--------:| :-------------|


### Présentation

Ces docker-compose permettent de déployer plusieurs services facilement et rapidement. Vous pouvez les utiliser avec Portainer directement ou via les commandes de docker-compose.
Tous les docker-compose sont commentés et sont configurés à l'aide de variables.

Ils intégrent tous le support de Traefik et de Loki.

# Debian

### Utilisation
Installation de Git :
```bash
 apt install -y git
```

Récupération des docker-compose :
```bash
git clone https://github.com/PAPAMICA/docker-compose-collection/
```


Configuration les variables et exécution d'un docker-compose :
```bash
cd docker-compose-collection
nano env
sudo docker-compose -f service.yml --env-file env up -d
```

# Portainer

UPDATE 2021 :
### Utilisation (2021)
Ajoutez l'URL de mon repo directement dans Portainer :
![PORTAINER](https://i.imgur.com/M49ssCN.png)


### Utilisation (2020)
+ 1 - Aller dans le sous menu "Stacks"
+ 2 - Cliquer sur "+ Add stack"
+ 3 - Nommer le stack dans le champs "Name"
+ 4 - Selectionner "Git Repository"
+ 5 - Repository URL : https://github.com/PAPAMICA/docker-compose-collection/
+ 6 - Compose path : service.yml
+ 7 - Ajouter les variables d'environnement requises "+ add environment variable"
+ 8 - Déployer avec le bouton "Deploy the stack"

![PORTAINER](https://zupimages.net/up/20/44/m6sv.png)


### Liste des docker-compose :

+ **Traefik**
+ **Portainer**
+ **Bookstack**
+ **CachetHQ**
+ **Zabbix-CachetHQ**
+ **Zabbix**
+ **Grafana**
+ **FileBrowser**
+ **FloodTorrent**
+ **Jellyfin**
+ **NextCloud**
+ **Odoo**
+ **Organizr**
+ **OwnCloud**
+ **Plex**
+ **RuTorrent**
+ **Seafile**
+ **TeamSpeak**
+ **SinusBot**
+ **TS3Viewer**
+ **VSCode**
+ **Website-HTML**
+ **Website-Wordpress**
     
Et bien plus sont à venir !
    
## Quelques commandes utiles :

Vu le nombre de personnes qui m’ont contacté suite aux précédents articles sur Tech2Tech.fr et Labo-Tech.fr  pour des commandes simples, voici celles que l’on m’a le plus demandées :

-   **docker container ls** : Afficher les containers Docker en cours
-   **docker-compose stop** : Arrêter les containers créés avec le scripts (dans le dossier du script)
- **docker-compose up -d** : Lancer les containers créés avec le scripts (dans le dossier du script)
-   **docker logs <id_container>** : Afficher les logs du container
-   **docker exec -it <id_container> bash** : Entrer dans le container 

Pour le reste des commandes, je vous invite à vous référer à mon article sur Labo-Tech :  [Quelles sont les commandes de base de Docker ?](https://labo-tech.fr/base-de-connaissance/quelles-sont-les-commandes-de-base-de-docker/)
