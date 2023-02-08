#stackoverflow https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python

#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python
chrome_options = Options()
chrome_options.add_argument("--kiosk")

#open driver
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome(executable_path='/tmp/chromedriver', chrome_options=chrome_options)


#go to website where images are
web_url = "https://en.wikipedia.org/wiki/Image"
driver.get(web_url)

#search for image by looking for keyword
im_link = driver.find_element_by_class_name("image")
im_link.click()
#open in new tab
#im_link.send_keys(Keys.CONTROL+Keys.RETURN)

#open new kiosk tab https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python

#identify element
m = driver.find_element_by_link_text("Help")
m.click()
#obtain parent window handle
p= driver.window_handles[0]
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)
print("Page title :")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
driver.switch_to.window(p)
print("Current page title:")
print(driver.title)
#close browser parent window
driver.quit()
