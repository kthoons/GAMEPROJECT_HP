from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]') # 성공

elem.click()

browser.switch_to_default_content() # 상위로 빠져 나옴
 
elem = browser.find_element_by_xpath('//*[@id="html"]') # 실패

time.sleep(5) # 5초 대기

browser.quit()


#//*[@id="html"]

