# Project Overview

- To install Docker and Dependencies you have to make a docker file there are a couple of things that you have to run
within the docker file.

* You have to have it set up like this

1. FROM ununtu:latest
2. ENV DEBIAN_FRONTEND=noninteractive
3. RUN apt-get -y update
4. RUN apt-get install -y apache2 curl
5. EXPOSE 80
6. WORKDIR /var/www/html
7. COPY index.html /var/www/html/index.html
8. ENTRYPOINT ['/usr/sbin/apache2ctl"]
9. CMD ["-D", "FOREGROUND"]

* When you run the container you have to run this command
* docker run -d --name apache1 apacheserver

# Docker Hub Repo. How to Create.


1. The first thing you want to do is make sure you have a Docker Account

2. click Repositoreis at the top in between Explore and Organizations.

3. Click Create Repository.

4. Name your Repo and make sure it is public and add a description and then click create.

# Allow DockerHub authentication Via CLI using Dockhub credentials

1. Log into hub.docker.com

2. Click on your username in the top right corner and select Account Settings

3. Add a description for your token

4. Copy the access tocken

5. and then you can use the token to use instead of your credentials. But be careful this token will only be displayed once.

6. When you configure github secrets It was super easy 

* Go to the main page of the repo

* Click settings

* Click Secrets

* Click New Repository Secret.

* Type a name for your secret


* Enter Value for the secret, in this case it was docker credentials, (Username) (Password)


# How to pull the project image

* First you have to clone your repo to your new EC2 instance.

* And then you have to start the process of building the image on your new instance.

* To start the build process you have to do these first steps

1. Make sure you DockerFile is good and there are no errors

2. Run docker build -t apacheserver

3. docker run -d --name apache1(Name of your choice) apacheserver

4. docker exec apache1 curl localhost


5. This is how you pull, build the docker image and container and verify the steps!


