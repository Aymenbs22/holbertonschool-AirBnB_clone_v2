#!/usr/bin/env bash
#bash script that setup nginx ....
#Bash script that sets up your web servers for the deployment of web_static. It must:

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR user:user /data/
sudo service nginx start
