#!/usr/bin/python
#
import time
from splinter import Browser
executable_path = {'executable_path':'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
browser = Browser(driver_name='chrome')
browser.visit('http://www2.jblearning.com/my-account/login')
browser.find_by_id('Content_C015_ctl00_ctl00_UserName_ctl00_ctl00_textBox_write').first.fill('nick.laff@fire.ca.gov')
browser.find_by_id('Content_C015_ctl00_ctl00_Password_ctl00_ctl00_textBox_write').first.fill('Calfire1!')
browser.find_by_id('Content_C015_ctl00_ctl00_CustomLoginButton').click()
time.sleep(3)
#browser.reload()
#browser.quit()
