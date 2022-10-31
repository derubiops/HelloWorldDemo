# Introduction to the HelloWorldDemo repository

Testing a multicontainer Hello World app with Nginx reverse proxy and SSL self-signed certificate.


## About this application

The application is based in two microservices running on Docker and wrapped with Docker Compose.

The app itself, a simple Python app to return the "hello world" sentence in json format and a reverse proxy that will serve the content of the app on port 443. If the application is requested on port 80, nginx will redirect it to port 443.

The solution has been written in Python, using Flask as a webserver, because it is a lightweight server that can asily executed on a Docker image. Also, Python provides greate readability.


### Pre-requisites

For local development, the following software has been used. This deployment has been developed and tested in Mac OS X Big Sur.

- Python 3.9. Install it from here https://www.python.org/downloads/
- Docker Desktop 20.10. Install it from https://docker-docs.netlify.app/compose/install/
- Docker Compose (already shipped with Docker Desktop)

__Note__: you only need to install Python locally if you want to execute the application "as is" directly with Python commands. Otherwise, only Docker Destktop is needed.


### Building the images

- __Hello World App__

  First, create a directory in your computer and checkout the code from this repo: https://github.com/derubiops/HelloWorldDemo
  ```
  mkdir HelloWorldDemo
  cd HelloWorldDemo
  git clone https://github.com/derubiops/HelloWorldDemo
  ```

  Get into the app directory
  ```
  cd helloworld/app
  ```

  Build the docker image so it will be available locally
  ```
  docker build --tag hello_world .
  ```

  Test the app on the Docker image:
  ```
  docker run --publish 8080:8080 hello_world
  ```
  
  Check with curl the response. 
  ```
   curl http://localhost:8080/hello
  ```
  
  You should see the following output in json format:
   ```
  {"hello":"world"}
  ```
  
  Alternatively, open a web browser and navigate to: http://localhost:8080/hello. The output should be the same.  

  
- __Nginx reverse proxy wrapped with Docker compose.__

  Note that the docker-compose.yml has defined two containers. One is the app itself and the other is the nginx that will act as reverse proxy.

  Navigate to the parent folder "helloworld" where the file docker-compose.yml is sitting and fire up Docker Composer:
  ```
  cd ..
  docker-compose up -d
  ```
  
  It will start creating the two containers and exposing nginx on the configured ports:
  ```
  docker-compose up -d
  Creating app ... done
  Creating nginx ... done
  ```
  
  Now the deployment should be running on ports 80 and 443. Check it with curl command again, but now you will not request the container endpoint but the nginx endpoint:
  ```
   curl http://localhost/hello
   <html>
   <head><title>301 Moved Permanently</title></head>
   <body>
   <center><h1>301 Moved Permanently</h1></center>
   <hr><center>nginx/1.23.2</center>
   </body>
   </html>
  ```
  
  This output is normal, as nginx is redirecting port 80 to 443. Try curl again with -kL modifiers:
  ```
  curl -Lk http://localhost/hello
  {"hello":"world"}
  ```
  Explanation: with "-L" curl will follow the redirection from port 80 to 443 and "-k" will disregard the certificate validation, as in this case is a self-signed certificate.
  
  Now, open a browser and navigate to http://localhost/hello to see the redirecttion from HTTP to HTTPS working. Expect to have the certificate warning due the certificate. To void this warning, you can install it locally.
  
  Once done, you can safely stop the containers:
  ```
  docker-compose down
  ```
  
