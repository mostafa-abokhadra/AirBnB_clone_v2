#!/usr/bin/env bash
# deploying webstatic
sudo apt-get update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
echo "almost there💚" | sudo tee -a /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]; then
        sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
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
sudo service nginx restart
