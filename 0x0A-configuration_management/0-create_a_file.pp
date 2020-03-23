# This will create a file with initial config
file {'/tmp/holberton':
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
