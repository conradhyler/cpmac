#!/usr/bin/python
#
import time
from splinter import Browser
<<<<<<< HEAD
executable_path = {'executable_path':'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
browser = Browser('iexplorer')
browser.visit('http://www2.jblearning.com/my-account/login')
browser.find_by_id('Content_C015_ctl00_ctl00_UserName_ctl00_ctl00_textBox_write').first.fill('nick.laff@fire.ca.gov')
browser.find_by_id('Content_C015_ctl00_ctl00_Password_ctl00_ctl00_textBox_write').first.fill('Calfire1!')
browser.find_by_id('Content_C015_ctl00_ctl00_CustomLoginButton').click()
=======
browser = Browser('chrome',incognito=True)
browser.visit('http://165.105.239.1/')
browser.fill('cprouterusername', 'admin')
browser.fill('cprouterpassword', 'fgfdgfds')
browser.find_by_id('button-1020-btnInnerEl').click()
>>>>>>> 433b15a99f4632008b7bcea3de34061eebdcc33d
time.sleep(3)
#browser.reload()
#browser.quit()
