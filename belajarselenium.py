from selenium import webdriver

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver1.get("https://twitter.com/")
driver2.get("https://www.twitch.tv/")
driver3.get("https://www.facebook.com/")