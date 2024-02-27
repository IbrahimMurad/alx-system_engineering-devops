# automatically configure an Ubuntu machine to respect the following requirements
#   Nginx should be listening on port 80
#   When querying Nginx at its root / with a GET request (requesting a page) using curl,
#     it must return a page that contains the string Hello World!
#   The redirection must be a “301 Moved Permanently”

exec { 'setup':
  provider => shell,
  command  => 'apt-get update; apt-get -y install nginx; ufw allow "Nginx HTTP"; echo "Hello World!" > /var/www/html/index.nginx-debian.html; sed -i "s/\tserver_name _;/\tserver_name _;\n\n\tlocation \/redirect_me {\n\n\t\treturn 301 https:\/\/www.youtube.com;\n\n\t}\n/" /etc/nginx/sites-enabled/default; service nginx restart',
}
