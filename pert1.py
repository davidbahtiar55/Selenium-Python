from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com")
#driver.find_element_by_name("username").send_keys("qaengineer")
# find_element = untuk mencari single elemen __ dilanjutkan dengan action
#driver.find_element_by_partial_link_text("Selenium").click()

#Elements
# link = driver.find_elements_by_tag_name("a")
# print(len(link))

# Class Name
#driver.find_element_by_class_name("radius").click()

#CSS Selector
#driver.find_element_by_css_selector("button.radius").click()

#Via Copy Selector
#driver.find_element_by_css_selector("#content > div > button").click()
#driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
#driver.find_element(By.XPATH,'//*[@id="content"]/div/button').click()

#New Tab
# time.sleep(2)
# driver.find_element_by_link_text("Click Here").click()
# time.sleep(2)
# driver.switch_to_window(driver.window_handles[0])
# driver.find_element_by_link_text("Click Here").click()
# time.sleep(2)
# driver.switch_to_window(driver.window_handles[0])
# driver.find_element_by_link_text("Click Here").click()
# time.sleep(2)
# driver.switch_to_window(driver.window_handles[0])
# driver.find_element_by_link_text("Click Here").click()
# time.sleep(2)
# driver.switch_to_window(driver.window_handles[0])

#Minimize & Maximize Windows
#driver.maximize_window()
#driver.minimize_window()