#!/usr/bin/python
#
import time
from splinter import Browser
browser = Browser('chrome',incognito=True)
browser.visit('http://165.105.239.1/')
browser.fill('cprouterusername', 'admin')
browser.fill('cprouterpassword', 'fgfdgfds')
browser.find_by_id('button-1020-btnInnerEl').click()
time.sleep(3)
#browser.reload()
browser.visit('http://165.105.239.1/admin/?v=6.4.0-91823d9-aer1600lpe#MacFilter')
time.sleep(1)
with open('/Users/conradhyler/Scripts/git/cpmac/mac.csv') as f:
    for line in f:
        browser.find_by_text('Add').click()
        browser.fill('addr', line)
        time.sleep(1)
        browser.find_by_text('OK').click()
        time.sleep(1)
        #browser.find_by_id('button-1005-btnEl').click()
        #browser.find_by_text('OK').click()
        #time.sleep(1)
        #browser.reload()



#browser.quit()
