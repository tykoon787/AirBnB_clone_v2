#!/usr/bin/env bash
# This script sets up a static web server
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo sed -i '$ a\<html><\n\t<title><p>Panda Practice</p></title>\n\t\t<body><h1>This is the body</h1>\n\t\t</body>\n</html>' /data/web_static/releases/test/index.html

## Create a symbolic link
sudo mkdir -p /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

## Changing ownership
sudo chown -R ubuntu:ubuntu /data/

## Serving content of /data/web_static/current/
sudo sed -i '/listen 80 default_server/a\\tlocation /hbnb_static {\n\t\talias /data/web/static/current/;\n\t}' /etc/nginx/sites-available/default

## Restart Service
sudo nginx -s reload

echo "This script finished"