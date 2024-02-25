# Puppet manifest to setup configs to ssh


file {'Declare_identity_file':
    ensure => present,
    path   => '~/.ssh/config'
    line   => 'IdentityFile ~/.ssh/school',
}

file {'Turn_off_passwd_auth':
    ensure => present,
    path   => '~/.ssh/config',
    line   => '\
    PasswordAuthentications no
    PreferredAuthentications publickey
    '
}
