# Puppet manifest to setup configs to ssh


file {'~/.ssh/config':
    ensure => present,
    line   => 'IdentifyFile ~/.ssh/school',
    path   => '~/.ssh/config'
}

file {'~/.ssh/config':
    ensure => present,
    line   => 'PreferredAuthentications publickey',
    path   => '~/.ssh/config'
}

file {'~/.ssh/config':
    ensure => present,
    line   => 'PasswordAuthentications no',
    path   => '~/.ssh/config'
}
