#!/usr/bin/env bash
#Manifest to install nginx
exec {'Install nginx':
command  => 'sudo apt update && sudo apt -y install nginx && echo "Holberton School" | sudo tee /var/www/html/index.html && redirect="\\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n" && sudo sed -i "37i $redirect" /etc/nginx/sites-enabled/default && sudo service nginx restart',
provider => shell,
}
