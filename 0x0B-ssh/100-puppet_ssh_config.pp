# Puppet manifest to setup configs to ssh


file {'~/.ssh/config':
    ensure => 'file',
    owner   => 'username',
    group   => 'username',
    mode    => '0600',
    content => "\
    Host server_alias
        HostName server_ip
        User your_username
        IdentityFile ~/.ssh/school
        PreferredAuthentications publickey
        PasswordAuthentication no
    ",
}
