# This is the manifest to fix wordpress using Puppet
exec { 'fixing http 500':
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
    path    => ['bin]
}
