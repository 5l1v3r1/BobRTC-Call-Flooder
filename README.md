# BobRTC-Call-Flooder
Used to open multiple tabs in BobRTC to call flood scammers.


Before you begin, you will need to do some setup.


# Installing Web Drivers

BobRTC-Call-Flooder requires specific web drivers depending on your drivers. 

If you use chrome, go to the following link and download the stable release: https://chromedriver.chromium.org/

If you use firefox, go to the following link and download the newest release: https://github.com/mozilla/geckodriver/releases

After downloading, put the exe file into C:\Windows if you are on windows, or if you use mac or linux put the file in your root directory.


# Running The Program

To use BobRTC-Call-Flooder you will need the latest version of Python which can be downloaded here: https://www.python.org/downloads/

After downloading Python, clone this repository and go into the directory.

Run: `pip install -r requirements.txt`

Run: `python run.py`

This will open the application. Next, go to https://bobrtc.tel, sign up, and go to the phonebook and pick a scammer.

Copy the link and put it in the box for BobRTC URL. 

Time between calls is the amount of time between a new tab opening.

Amount of calls is how many tabs will be opened.

Refresh interval is the amount of time to wait before refreshing each page.

Finally, pick the web browser you have installed and click Send Calls.

**The browser must not be minimized or else it will not work!**
