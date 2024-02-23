# Puppet manifest to install flask

package{ 'python':
  ensure => '3.8.10'
}
package{ 'werkzeug':
  ensure => '2.1.1',
}

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python', 'werkzeug']
}

