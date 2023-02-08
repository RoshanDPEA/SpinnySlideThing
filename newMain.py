#stackoverflow https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python

#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open driver
driver = webdriver.Firefox()

#(optional) save window handle
#tab_before = driver.window_handles[0]

#go to wikipedia page
web_url = "https://en.wikipedia.org/wiki/Adam_Bede"
driver.get(web_url)

#find image link
im_link = driver.find_element_by_class_name("image")

#open in new tab
im_link.send_keys(Keys.CONTROL+Keys.RETURN)

#(optional) save new window handle
#tab_after = driver.window_handles[0]

#(optional) switch back to first tab:
#driver.switch_to_window(tab_before)
