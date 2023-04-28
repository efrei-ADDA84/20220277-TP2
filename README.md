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
