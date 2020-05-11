from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_id("treasure")
	attribute = x_element.get_attribute("valuex")
	y = calc(attribute)
	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)
	robot_checkbox = browser.find_element_by_id("robotCheckbox").click()
	robot_radiobutton = browser.find_element_by_id("robotsRule").click()
	
	button = browser.find_element_by_tag_name("button")
	button.click()

finally:
	time.sleep(10)
	browser.quit()
