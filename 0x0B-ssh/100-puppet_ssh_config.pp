# set up client SSH configuration file so that he can connect to a server without typing a password.

file_line { 'ssh config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '#    IdentityFile',
  match  => '#    IdentityFile ~/.ssh/school',
}


file_line { 'ssh config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '^#   PasswordAuthentication',
  match  => '^#   PasswordAuthentication no',
}
