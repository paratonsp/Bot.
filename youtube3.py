from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import webbrowser
import time

# path for the driver
driver = webdriver.Chrome(executable_path="C:\mydriver\chromedriver")

driver.get("https://www.google.com")
driver.execute_script("window.open ('https://www.google.com', 'new window')")
driver.switch_to.window(driver.window_handles[0])

for page in ("https://www.bing.com", "https://www.facebook.com"):
    driver.execute_script(f"window.open ('{page}')")
driver.switch_to.window(driver.window_handles[1])

time.sleep(60)
