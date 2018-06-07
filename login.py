import getpass
import pexpect
import time
#s = pxssh.pxssh()
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
hostname2 = ('@'+hostname)
print(hostname2)
userhost = (username+hostname2)
print(userhost)
#s.login(hostname, username, password)
#s.sendline('ls')   # run a command
#s.prompt()             # match the prom
child = pexpect.spawn('/usr/bin/ssh '+userhost)
child.expect('password:', timeout=120) 
#time.sleep(1)
child.sendline(password)
time.sleep(2)
child.expect('$',timeout=60)
child.sendline('get /config/firewall')
child.expect('$', timeout=60)
time.sleep(2)
print child.before, child.after

