# Creating file in /tmp/school

file { '/tmp/school' :
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0774',
  content => 'I love Puppet'
}

