import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.youtube.com/watch?v=l9N0koCYSuA")
# player_status = driver.execute_script(
#     "return document.getElementById('movie_player').getPlayerState()"
# )
time.sleep(90)
