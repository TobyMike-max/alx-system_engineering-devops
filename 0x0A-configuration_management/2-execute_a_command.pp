# Executes a command to create a manifest
exec {'killmenow':
  path    => ['/usr/bin'],
  command => 'pkill -f killmenow'
}
