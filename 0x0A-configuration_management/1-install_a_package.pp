# Puppet manifest to install flask

package{ 'werkzeug':
  ensure   => present,
}

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug']
}

