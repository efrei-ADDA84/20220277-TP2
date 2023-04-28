# 20220277-TP2

# DevOps - TP2 - Weather scrapper API

<image src="https://bump.sh/packs/static/3e19c626035098dcd33c.png" width=800 center>

[![Downloads](https://static.pepy.tech/personalized-badge/docker?period=month&units=international_system&left_color=blue&right_color=yellow&left_text=docker)](https://pepy.tech/project/docker)   [![Downloads](https://static.pepy.tech/personalized-badge/requests?period=month&units=international_system&left_color=brightgreen&right_color=orange&left_text=requests)](https://pepy.tech/project/requests) [![Downloads](https://static.pepy.tech/personalized-badge/openweather?period=month&units=international_system&left_color=blue&right_color=green&left_text=openweather)](https://pepy.tech/project/openweather) [![Downloads](https://static.pepy.tech/personalized-badge/github?period=month&units=international_system&left_color=black&right_color=orange&left_text=github)](https://pepy.tech/project/github) [![GitHub Actions](https://github.com/actions/toolkit/actions/workflows/main.yml/badge.svg)](https://github.com/actions/toolkit/actions/workflows/main.yml)

> ### Objectifs
> - Objectifs
> - Configurer un workflow Github Action
> - Transformer un wrapper en API
> - Publier automatiquement a chaque push sur Docker Hub
> - Mettre à disposition son image (format API) sur DockerHub
> - Mettre à disposition son code dans un repository Github

> ### Prérequis
> - Docker
> - Github

> ### 1. Configuration d"un workflow Github Action
- Créer le fichier `.github/workflows/post-on-dockerhub.yml` 
- Ajouter le contenu suivant :
````
name: build-deploy-on-dockerhub

run-name: ${{ github.actor }} is building a Docker image
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Build docker image
        run: docker build . -t weather:0.0.3
      - name: Login to docker hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Create docker image tag
        run: docker tag weather:0.0.3 ${{ secrets.DOCKER_USER_REGISTRY }}/weather:0.0.3
      - name: Push to docker hub
        run: docker push ${{ secrets.DOCKER_USER_REGISTRY }}/weather:0.0.3
````

Cette configuration permet de:
- Construire l'image docker
- Se connecter à docker hub
- Créer un tag sur docker hub
- Push l'image sur docker hub

À la fin de la configuration, le workflow Github Action est disponible sur Github après push et biensûr paramétrage des `secrets` utilisés. Si les secrets ne sont pas paramétrés, vous aurez une erreur d'éxécution.

> ### 2. Transmation de notre wrapper Weather en API
Pour se faire noous allons utiliser `Flask` pour transformer notre code en API. 
- Installer flask
- Créer un fichier `main.py`
- Faire les importations
- Définir la méthode qui renvoie le résultat avec l'annotation `@app.run()`
- Définir la méthode qui renvoie le résultat avec l'annotation `@app.route('/weather')`
- ***(ACTION OPTIONNELLE)*** Vous pouvez préciser la méthode `GET` mais c'est elle qui est prise par défaut.

Une fois notre code prêt, nous pouvons tester en démarrant le serveur avec l'API_KEY en paramatres.
> $ API_KEY="VOTRE-API-KEY" python main.py \

Lorsque le serveur tourne sans erreur, nous aurez un résultat comme suit:
````
* Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8081
 * Running on http://10.3.200.190:8081
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 770-403-475
````
Notre API est donc accessible à l'adresse `http://127.0.0.1:8081`. Avec ce lien, nous allons pour pouvoir tester la méthode `GET` sur notre API en passant la longitude et la latitude en paramètre de l'API comme suit : `http://127.0.0.1:8081/weather?lat=5.902785&long=102.754175`.

> ### 3. Publier automatiquement a chaque push sur Docker Hub
Cete est réalisé automatiquement lorsqu'on fait un push sur GitHub car nous avons déjà configuré le workflow Github Action.

> ### 4. Tester l'API
- Test sur l'image en local
```
$ docker run  --env API_KEY="VOTRE-API-KEY"  weatherapi:0.0.1
```
Ensuite nous pouvons tester la méthode `GET` sur notre API en passant la longitude et la latitude en paramètre de l'API comme suit : `http://127.0.0.1:8081/weather?lat=5.902785&long=102.754175`.

- Test de l'image depuis DockerHub
```
$ docker run -p 8081:8081 --env API_KEY="VOTRE-API-KEY" anicetdevops/weatherapi:0.0.1  
```
Ensuite nous pouvons tester la méthode `GET` sur notre API en passant la longitude et la latitude en paramètre de l'API comme suit : `http://127.0.0.1:8081/weather?lat=5.902785&long=102.754175`.

>
> Etudiant: AGBONON EDAGBDJI Yao Anicey \
> Promo: BDML 2024 \
> Email: yao-anicet.agbonon-edagbedji@efrei.net
>