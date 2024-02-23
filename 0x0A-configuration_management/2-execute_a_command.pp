# Puppet manifest to kill runnin process call killmenow

exec{'pkill':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/ps aux | /usr/bin/pgrep killmenow'
}

