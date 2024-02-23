# install flask version 2.1.0 from pip3.

package { 'Flask':
  name            => 'flask'
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options => ['--user'],
}
