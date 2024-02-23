# install flask version 2.1.0 from pip3.

exec { 'flask-install':
  command => '/usr/bin/pip3 install Flask==2.0.1'
}
