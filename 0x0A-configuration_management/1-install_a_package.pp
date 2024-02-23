# Puppet manifest to install flask

package{ 'werkzeug':
  ensure   => present,
  provider => 'pip3'
}

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug']
}

