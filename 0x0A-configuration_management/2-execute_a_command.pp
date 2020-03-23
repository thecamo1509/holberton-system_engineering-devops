# This manifest will terminate a process called killmenow
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
