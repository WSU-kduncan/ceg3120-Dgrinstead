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



