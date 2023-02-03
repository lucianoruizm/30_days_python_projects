from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

profile_path = r'C:/Users/BatLuciano/AppData/Roaming/Mozilla/Firefox/Profiles/uwaqfpn5.default-release'
# Create Firefox options
options = Options()
# options.add_argument("-profile")
# options.add_argument(FirefoxProfile.DEFAULT_PREFERENCES)

# Set the download directory
# profile = webdriver.FirefoxProfile("C:/Users/BatLuciano/AppData/Roaming/Mozilla/Firefox/Profiles/uwaqfpn5.default-release")
# profile.set_preference("browser.download.folderList", 2)
# profile.set_preference("browser.download.dir", "C:/Users/BatLuciano/Documents/descargarSelenium")
# options.profile = profile

options.set_preference('profile', profile_path)

# Create an instance of FirefoxDriver
# driver = webdriver.Firefox(options=options)

# browser = webdriver.Firefox(profile)
# browser.get()

# Create an instance of FirefoxDriver
driver = webdriver.Firefox(options=options)

# Open the website
driver.get("https://file-examples.com")

# Locate the button element
button = driver.find_element(By.CSS_SELECTOR, "div.col-md-4:nth-child(3) > div:nth-child(1) > a:nth-child(4)")
# Click the button
button.click()

button2 = driver.find_element(By.CSS_SELECTOR, "tr.odd:nth-child(1) > td:nth-child(3) > a:nth-child(1)")
button2.click()

button3 = driver.find_element(By.CSS_SELECTOR, "tr.odd:nth-child(1) > td:nth-child(5) > a:nth-child(1)")
button3.click()

