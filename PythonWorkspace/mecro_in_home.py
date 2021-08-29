### 최종 프로그램 ###

from PIL.ImageOps import grayscale
import requests 
import re
from selenium import webdriver

import time
import pyautogui
from random import *
import pyperclip


url = "https://work.carefor.co.kr/#cGFnZXx7J3R5cGUnOidsZWZ0X3N1YjEnLCAndmlldyc6Jy9wYXRpZW50L3ZpZXcucGF0aWVudF9tYW5hZ2UnfSV7InRpdGxlIjoiMS0xLuyImOq4ieyekOygleuztCDqtIDrpqwiLCJldmFsIjoiNDciLCJtb3ZlX3Njcm9sbCI6dHJ1ZX18bGVmdF9zdWIx"
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(url)
browser.maximize_window()
id = ["14146000562","전현미","9810"]

for i in range(1,4):
    browser.find_element_by_xpath(f"//*[@id='login_outline']/div[1]/div/form/ul/li[{i}]/input").send_keys(id[i-1])

browser.find_element_by_class_name("btn").click()

time.sleep(2)

# 팝업 창
pyautogui.click(pyautogui.locateOnScreen("mecro_img/close.png"))
time.sleep(0.2)

browser.find_element_by_xpath("//*[@id='layerModal']/div/div[3]/div[7]/span").click()
time.sleep(0.2)
# 왼쪽 6번 버튼
browser.find_element_by_xpath("//*[@id='left_area']/div[4]/ul/li[6]").click()
# 6번 세부버튼
browser.find_element_by_xpath("//*[@id='left_sub6']/div[2]/table/tbody/tr[2]/td/div/ul/li[3]").click()
time.sleep(0.5)




def do_text():
    time.sleep(0.3)
    pyautogui.scroll(400)
    time.sleep(0.3)

    rk = []
    rand_n = choice([0,1])

    # 5층
    for i in pyautogui.locateAllOnScreen("mecro_img/5floor.png", grayscale=True):
        rk.append(i)
    pyautogui.click(rk[rand_n])
    
    time.sleep(0.3)
    browser.find_element_by_xpath("//*[@id='tbl_manageDailyNight']/tbody/tr[18]/td[2]/textarea").click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    time.sleep(0.1)
    rk = []
    rand_n = choice([0,1])

    # 6층
    for i in pyautogui.locateAllOnScreen("mecro_img/6floor.png", grayscale=True):
        rk.append(i)
    
    pyautogui.click(rk[rand_n])
    
    time.sleep(0.3)
    browser.find_element_by_xpath("//*[@id='tbl_manageDailyNight']/tbody/tr[18]/td[2]/textarea").click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    time.sleep(0.1)
    # 저장 버튼
    # browser.find_element_by_class_name("btn_type1").click()
    # time.sleep(0.1)
    # 취소 버튼
    browser.find_element_by_class_name("btn_type3").click()
    time.sleep(0.3)

def do_2(i):
    try:
        #이름 선택
        browser.find_element_by_xpath(f"//*[@id='daily_check_list']/table/tbody/tr[{i}]/td[2]").click()
        
        do_text()
    except:
        print("직접 수정",j,k)
        

def do_3(i):
    try:
        #이름 선택
        browser.find_element_by_xpath(f"//*[@id='daily_check_list']/table/tbody/tr[{i}]/td[3]").click()
        
        do_text()
    except:
        print("직접 수정",j,k)





start = 1  # 3월 첫 째 주 시작 갯수
T1 = [1,3,5,7,8,10,12]
T0 = [4,6,9,11]
T2 = [2]

for i in range(0,1):

    for j in range(1,13):

        if j in [3,4,5,6,7,8,9,10,11,12]:
            time.sleep(0.2)
            # 날짜 설정 버튼
            browser.find_element_by_class_name("s3").click()
            time.sleep(0.2)

            pyautogui.click(pyautogui.locateOnScreen("mecro_img/button.png"))
            time.sleep(0.1)

            # 년도 선택
            pyautogui.click(pyautogui.locateOnScreen(f"mecro_img/202{i}.png"))

            # 월 선택
            pyautogui.click(pyautogui.locateOnScreen(f"mecro_img/{j}m.png"))
            time.sleep(0.3)



            if j in T0 :
                for k in range(1,31):
                    res = (30 - start)//7
                    rem = (30 - start) % 7
                    if k in range(1, start+1):
                        if k == 1:
                            do_3(k)
                        else:
                            do_2(k)
                    elif k in range(start+1, start+(res*7)+1 ):
                        if k in range(start+1, start+(res*7)+1, 7):
                            do_3(k)
                            if k == 30:
                               start = 7-rem
                        else:
                            do_2(k)
                            if k == 30:
                               start = 7-rem
                    else:
                        if k == start+(res*7)+1 :
                            do_3(k)
                            if k == 30:
                               start = 7-rem
                        else:
                            do_2(k)
                            if k == 30:
                               start = 7-rem

                   
            elif j in T1:
                for k in range(1,32):
                    
                    res = (31 - start)//7
                    rem = (31 - start) % 7
                    if k in range(1, start+1):
                        if k == 1:
                            do_3(k)
                        else:
                            do_2(k)
                    elif k in range(start+1, start+(res*7)+1 ):
                        if k in range(start+1, start+(res*7)+1, 7):
                            do_3(k)
                            if k == 31:
                                start = 7 - rem
                        else:
                            do_2(k)
                            if k == 31:
                                start = 7 - rem
                    else:
                        if k == start+(res*7)+1 :
                            do_3(k)
                            if k == 31:
                                start = 7 - rem
                        else:
                            do_2(k)
                            if k == 31:
                                start = 7 - rem

            else:
                for k in range(1,29):
                 
                    res = (28 - start)//7
                    rem = (28 - start) % 7
                    if k in range(1, start+1):
                        if k == 1:
                            do_3(k)
                        else:
                            do_2(k)
                    elif k in range(start+1, start+(res*7)+1 ):
                        if k in range(start+1, start+(res*7)+1, 7):
                            do_3(k)
                            if k == 28:
                                start = 7-rem
                        else:
                            do_2(k)
                            if k == 28:
                                start = 7-rem
                    else:
                        if k == start+(res*7)+1 :
                            do_3(k)
                            if k == 28:
                                start = 7-rem
                        else:
                            do_2(k)
                            if k == 28:
                                start = 7-rem
            time.sleep(0.5)
                

