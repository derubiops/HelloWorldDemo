# Introduction to the HelloWorldDemo repository

Testing Hello World app with Nginx reverse proxy to deploy it to a Kubernetes testin environment.

This is intended for demo only but it has been taken into consideration different aspects to deploy it to production.

## About this application

The application is based in two microservices running on Docker.

The app itself, a simple Python app to return the "hello world" sentence in json format and a reverse proxy that will serve the content of the app on ports 80 and 443.

### Pre-requisites

For local development, the following software has been used:

Python 3.9
Flask 2.2.2
Docker Desktop 20.20 (client)
Docker Desktop 20.20 (server)
Minikube

### Building the images
