# Setup Load Balancing TODOs


* The standard information in the /etc/hosts file is going to be the standard IP address. I changed it to the name of
the instance. For example like proxy, srv1 and srv2.

* You can SSH in between systems using Private IPs by using the HAProxy. 
# HAProxy configuration & documentation requirements


* There are a couple of different ways that you can install haproxy. You can do it from your CF template. Or you can do it directly from the command line. I installed it from my cf template just because it is going to install it exactly how you need it installed instead of going through the command line and worrying if you missed a step or not.

* The way that you install haproxy is apt-get install haproxy && \ And this is doing it from the cf template

* If you do it from the command you have to go throug and run everyting as sudo so it installs correctly

* You are going to have front end files and backend files. You need to modify both files if necessary

* To reboot ha proxy you have to do "sudo systemctl restart haproxy"



* The only files that should really be modified is the front end and back end settings.

* To restart haproxy you want to run sudo service haproxy restart

* 
