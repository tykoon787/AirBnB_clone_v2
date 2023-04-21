#!/usr/bin/env bash
# This script sets up a static web server

## Install nginx
sudo apt-get install nginx

## Create directories and sub-dirs
### releases
mkdir -p /data/web_static/releases/

### shared
mkdir -p /data/web_static/shared

### releases/test
mkdir -p /data/web_static/releases/test

### Index.html
touch /data/web_static/releases/test/index.html
sed -i '$ a\<html><\n\t<title><p>Panda Practice</p></title>\n\t\t<body><h1>This is the body</h1>\n\t\t</body>\n</html>' index.html

## Create a symbolic link
mkdir /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

## Changing ownership
sudo chown -R ubuntu:ubuntu /data/

## Serving content of /data/web_static/current/
sed -i '/server_name _;/a\\tlocation /hbnb_static {\n\t\t alias /data/web/static/current/;\n\t}' /etc/nginx/sites-available/default

## Restart Service
sudo service nginx restart