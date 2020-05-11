from selenium import webdriver
import math
import time


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	time.sleep(2)
	
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	#/html/body/div/form/div[1]/label/span[2] //*[@id='input_value'] 
	answer = browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox.form-check-input").click()
	robot_radiobutton = browser.find_element_by_css_selector("#robotsRule.form-check-input").click()
	
	button = browser.find_element_by_css_selector("button.btn.btn-default").click()

finally:
	time.sleep(10)
	browser.quit()
