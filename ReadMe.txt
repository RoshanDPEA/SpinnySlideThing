For this project to get the code working on the raspberry pi follow these intructions https://patrikmojzis.medium.com/how-to-run-selenium-using-python-on-raspberry-pi-d3fe058f011
Guess and check the chrome driver version that works with chromium because regtular google chrome does not work on the raspberry pi without and emulataor and that is more of a hastle than guessing nd checking

also add this at the start it wont work without it dont remove it just leave it there
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--kiosk")

also if dual screens doesnt work add this to the config.txt file on the raspberry pi and go to screen configurations and activate the HMDI port that isnt working
https://support.thepihut.com/hc/en-us/articles/360015638017-Raspberry-Pi-dual-display-second-screen-not-working

also run with admin privilgages with sudo and to install package do sudo pip3 install PackageName
to run the code use sudo python3 newMain.py

to get to to grab a perticular image just change the web url to the website you want and use find by HTML tag to search for the image
