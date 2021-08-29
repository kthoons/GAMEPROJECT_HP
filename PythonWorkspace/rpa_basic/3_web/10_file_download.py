from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': r'C:\Users\강태훈\Desktop\PythonWorkspace'})

browser = webdriver.Chrome(options = chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to_frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(3)
browser.quit()
