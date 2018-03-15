from splinter import Browser
browser = Browser('chrome')
browser.visit('http://google.com')
# Note: 'q' is the value of the atribute 'name', not the 'id'
# <input type='text' name='q'...
browser.fill('q', 'the answer to life the universe and everything')
# find the submit buttom by the class atribute and click it
browser.find_by_css('.lsb').first.click()
# Note: find_by_css find elements in html using css selectors
# like we use in a css file
print browser.find_by_css('#topstuff .std h2').first.value

browser.quit()