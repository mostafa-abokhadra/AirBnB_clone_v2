#!/usr/bin/env bash
# deploying webstatic
sudo apt_get update
sudo apt_get install nginx
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
cd /data/web_static/releases/test/
echo "almost there💚" >> index.html
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu
sudo sed -i '$ a \
\
server {\
    listen 80;\
    server_name bukhadra.tech;\
\
    location /hbnb_static {\
        alias /data/web_static/current/;\
    }\
\
}\
' /etc/nginx/sites-available/default
