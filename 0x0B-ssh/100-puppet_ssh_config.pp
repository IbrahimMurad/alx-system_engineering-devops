# set up client SSH configuration file so that he can connect to a server without typing a password.

include stdlib


file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '^#   PasswordAuthentication no',
  match  => '^#   PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '^#    IdentityFile ~/.ssh/school',
  match  => '^#    IdentityFile',
}
