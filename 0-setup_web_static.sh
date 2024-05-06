#!/usr/bin/env bash
# setup a web serer for the deployment of web_static

apt update -y
apt install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<!DOCTYPE html><html><head></head><body><p>Nginx server test</p></body></html>" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data

path="/etc/nginx/sites-available/default"
dir="location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
if ! grep -q "location /hbnb_static/" $conf_path
then
    sudo sed -i "s/^\tserver_name _;/\tserver_name _;\n\t$dir/" $path
fi
sudo service nginx restart
