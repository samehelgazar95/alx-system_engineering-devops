# Puppet manifest to install flask

package{ 'python':
  ensure => '3.8.10'
}
package{ 'werkzeug':
  ensure => present,
}

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python', 'werkzeug']
}

