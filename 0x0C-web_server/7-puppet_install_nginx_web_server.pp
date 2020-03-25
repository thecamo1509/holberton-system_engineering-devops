#!/usr/bin/env bash
#Manifest to install nginx
exec { 'Nginx install'
  command  => 'sudo apt -y update && sudo apt -y install nginx && echo "Holberton School" >> /var/www/html/index.html && direction= "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "35i $direction" /etc/nginx/sites-enabled/default && service nginx start',
  provider => shell,
}
