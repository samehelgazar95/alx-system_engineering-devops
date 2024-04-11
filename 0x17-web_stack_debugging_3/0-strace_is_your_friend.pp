# replace 'phpp' with 'php' in 'wp-settings.php'

exec{'fix-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path 	=> '/var/local/bin/:/bin/'
}

