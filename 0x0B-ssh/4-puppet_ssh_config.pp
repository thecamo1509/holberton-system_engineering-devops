 
#!/usr/bin/env bash
# puppet manifest to modify ssh_config
file {'/etc/ssh/ssh_config':
ensure => present,
}->
file_line { 'Set passauth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
match  => '^PasswordAuthentication.*$',
}->
file_line {'set identityfile':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/holberton',
match  => '^IdentyFile.*$',
}
