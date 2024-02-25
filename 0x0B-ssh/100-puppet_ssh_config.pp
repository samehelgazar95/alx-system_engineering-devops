# Puppet manifest to setup configs to ssh


file_line {'Declare identity file':
    ensure => 'present',
    path   => '~/.ssh/config'
    line   => 'IdentityFile ~/.ssh/school',
}

file_line {'Turn off passwd auth':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => "PasswordAuthentication no"
}
