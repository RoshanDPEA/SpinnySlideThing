#stackoverflow https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python

#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import _thread as thread
import threading
import time
from time import sleep

def imageUpdate():
    # https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python
    chrome_options1 = Options()
    chrome_options1.add_argument("--kiosk")

    # open driver
    # https://chromedriver.chromium.org/getting-started
    driver1 = webdriver.Chrome(executable_path='/home/student/Documents/chromedriver', chrome_options=chrome_options1)

    driver1.set_window_position(2000, 0)

    # go to website where images are
    web_url1 = "https://en.wikipedia.org/wiki/Image"
    driver1.get(web_url1)

    # https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python
    # search for image by looking for keyword
    im_link1 = driver1.find_element_by_class_name("image")
    # im_link.click()
    # open in new tab
    im_link1.send_keys(Keys.CONTROL + Keys.RETURN)

    # open new kiosk tab
    # #https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python

    # choose where to open tab
    # https://stackoverflow.com/questions/3816073/in-a-multi-monitor-display-environment-how-do-i-tell-selenium-which-display-to
    # have a second thread control the second monitor
    driver1.set_window_position(2000, 0)

    # identify element
    # m = driver.find_element_by_link_text("Help")
    # m.click()
    # obtain parent window handle

    # https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python closing tabs
    p1 = driver1.window_handles[1]
    driver1.switch_to.window(p1)

    while True:
        sleep(15)

    """"
    #m.click()
    # obtain parent window handle
    p = driver.window_handles[0]
    # obtain browser tab window
    #c = driver.window_handles[1]
    # switch to tab browser
    driver.switch_to.window(c)
    print("Page title :")
    print(driver.title)
    # close browser tab window
    driver.close()
    # switch to parent window
    driver.switch_to.window(p)
    print("Current page title:")
    #print(driver.title)
    # close browser parent window
    driver.quit()
    """



#https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python
chrome_options = Options()
chrome_options.add_argument("--kiosk")

#open driver
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome(executable_path='/home/student/Documents/chromedriver', chrome_options=chrome_options)


#go to website where images are
web_url = "https://en.wikipedia.org/wiki/Image"
driver.get(web_url)

#https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python
#search for image by looking for keyword
im_link = driver.find_element_by_class_name("image")
#im_link.click()
#open in new tab
im_link.send_keys(Keys.CONTROL+Keys.RETURN)

#open new kiosk tab
# #https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python

#choose where to open tab
#https://stackoverflow.com/questions/3816073/in-a-multi-monitor-display-environment-how-do-i-tell-selenium-which-display-to
#have a second thread control the second monitor

#identify element
#m = driver.find_element_by_link_text("Help")
#m.click()
#obtain parent window handle

#https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python closing tabs
p= driver.window_handles[0]
driver.switch_to.window(p)

driver.switch_to.window(p)
driver.close()




"""
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)
print("Page title :")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
#driver.switch_to.window(p)
print("Current page title:")
#print(driver.title)
#close browser parent window
driver.quit()

"""

#second monitor

#thread.start_new_thread(imageUpdate(), ())

thr = threading.Thread(target=imageUpdate())
thr.start()
