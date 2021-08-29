import time
from selenium import webdriver

F_name = "나도"
L_name = "코딩"
Country = "Canada"
Subject = "퀴즈 완료하였습니다."

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com")
browser.maximize_window()

browser.find_element_by_link_text('Learn HTML').click()
# browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()

browser.find_element_by_link_text('HOW TO').click()
# browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

browser.find_element_by_link_text('Contact Form').click()

browser.find_element_by_id('fname').send_keys(F_name)
browser.find_element_by_id('lname').send_keys(L_name)

browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(Country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(Subject)

time.sleep(5)

browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()