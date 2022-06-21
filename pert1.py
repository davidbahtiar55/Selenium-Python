from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
#driver.find_element_by_name("username").send_keys("qaengineer")
# find_element = untuk mencari single elemen __ dilanjutkan dengan action
#driver.find_element_by_partial_link_text("Selenium").click()

#Elements
link = driver.find_elements_by_tag_name("a")
print(len(link))