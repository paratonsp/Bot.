from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import psutil

search = "Demo Background Sample Video"

while True:
    option = Options()
    option.add_argument("--window-size=320,480")
    # proxyAddress = "103.103.88.162"
    # option.add_argument(f"--proxy-server={proxyAddress}")

    browser = webdriver.Chrome("./chromedriver", options=option)

    url = "https://www.youtube.com/results?search_query="
    url += search
    browser.get(url)

    browser.find_element(
        By.XPATH, '//yt-formatted-string[text()="' + search + '"]'
    ).click()

    time.sleep(90)
