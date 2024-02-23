# Puppet manifest to create

file{ '/tmp/school':
ensure  => 'file',
owner   => 'www-data',
group   => 'www-data',
mode    => '0774',
content => 'I love Puppet',

}

