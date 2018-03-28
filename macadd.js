var SSH = require('simple-ssh');
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')

var ssh = new SSH({
    host: hostname,
    user: username,
    pass: password
});

ssh.exec('echo $PATH', {
    out: function(stdout) {
        console.log(stdout);
    }
}).start();

/*** Using the `args` options instead ***/
ssh.exec('echo', {
    args: ['$PATH'],
    out: function(stdout) {
        console.log(stdout);
    }
}).start();