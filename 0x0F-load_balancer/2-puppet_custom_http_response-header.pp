#!/usr/bin/env bash
#Manifest to apply headers
exec {'Install nginx':
command  => 'sudo apt update && sudo apt -y install nginx && echo "Holberton School" >> /var/www/html/index.html && sudo sed -i "60i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
provider => shell,
}
