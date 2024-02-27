# automatically configure an Ubuntu machine to respect the following requirements
#   Nginx should be listening on port 80
#   When querying Nginx at its root / with a GET request (requesting a page) using curl,
#     it must return a page that contains the string Hello World!
#   The redirection must be a “301 Moved Permanently”

include stdlib

package { 'nginx':
  ensure   => latest,
  provider => 'apt',
}

package { 'ufw':
  ensure => latest,
}

exec { 'listen to 80':
  command => '/usr/sbin/ufw allow Nginx HTTP',
  require => Package['ufw', 'nginx'],
}

file { 'main page':
  path    => '/var/www/html/index.nginx-debian.html',
  ensure  => present,
  require => Package['nginx'],
  content => 'Hello World!"\n"',
}
