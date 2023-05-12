from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil
from random import randrange
from threading import Thread
import tkinter as tk

search = "Demo Background Sample Video"


def open_youtube():
    root = tk.Tk()
    width = 320
    height = 480

    screen_width = root.winfo_screenwidth() - width
    screen_height = root.winfo_screenheight() - height

    option = Options()
    option.add_argument(f"--window-size={width},{height}")
    option.add_experimental_option("excludeSwitches", ["enable-logging"])

    # browser = webdriver.Chrome("./chromedriver", options=option)
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=option
    )
    browser.set_window_position(
        randrange(screen_width), randrange(screen_height), windowHandle="current"
    )

    url = "https://www.youtube.com/results?search_query="
    url += search

    try:
        browser.get(url)
        try:
            browser.find_element(
                By.XPATH, '//yt-formatted-string[text()="' + search + '"]'
            ).click()
            time.sleep(10)
            browser.quit()
        except:
            browser.quit()
            pass
    except:
        browser.quit()
        pass


if __name__ == "__main__":
    totalCount = 0
    while True:
        while psutil.virtual_memory().percent < 70:
            time.sleep(3)
            t = Thread(target=open_youtube, daemon=True)
            t.start()

            totalCount += 1
            print(f"Window Open: {totalCount}")
