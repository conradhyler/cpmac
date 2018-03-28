import getpass
import pexpect
import time
import sys
#s = pxssh.pxssh()
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
hostname2 = ('@'+hostname)
userhost = (username+hostname2)
#s.login(hostname, username, password)
#s.sendline('ls')   # run a command
#s.prompt()             # match the prom
child = pexpect.spawn('/usr/bin/ssh '+userhost)
child.logfile = sys.stdout
child.expect('password:',timeout=120)
#print child.before, child.after
#time.sleep(1)
child.sendline(password)
child.sendcontrol('m')
time.sleep(2)
child.expect('$',timeout=60)
#print child.before, child.after
child.sendline('get /config/firewall')
child.logfile = sys.stdout
child.expect('$', timeout=60)
time.sleep(2)
print child.before, child.after

