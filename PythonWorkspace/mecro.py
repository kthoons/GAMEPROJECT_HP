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
browser = webdriver.Chrome("C:\\Users\\강태훈\\Desktop\\chromedriver\\chromedriver.exe")
browser.get(url)
browser.maximize_window()
id = ["14146000562","전현미","9810"]


daily_5 = ["장현준어르신 보호자께서 호박죽 가져다`줌",
"김종남어르신 연탄간다고 자주 거실로 나오심",
"권계행어르신 계속 소리를 지르심",
"박영심어르신 밤 12시에 주무시지않고 배회하셔서 취침유도해드림",
"장현준어르신 밤새도록 침대난간을 똑똑 두드림",
"김종남어르신 밤 늦게까지 중얼거리며 혼잣말 하시다가 주무심",
"윤준섭어르신 변을 시트와 바닥에 오염시켜서 교체해드림",
"심상순어르신 옷을 다 벗고 변으로 다 오염시켜서 교체해드렸는데 새벽에 또 반복하심",
"이창석어르신 밤에 자주 거실로 나오심",
"강경숙어르신 기저귀에 변을 많이 보심(설사는 아님)",
"장현준어르신 침대난간을 쳐서 옆방에 어르신 잠을 설침",
"윤준섭어르신 침상밖으로 나오실려고 하셔서 주무시는 동안 옆에 같이 있었음",
"강경숙어르신 등쪽에 발적이 보여서 체위해드렸습니다.",
"유선례어르신 아침 식사를 못하심(케어윌한잔드림)",
"박안순어르신 엉덩이쪽 발적보여서 연고랑 체위변경해드림",
"장현준어르신 소리를 지르심",
"김정자어르신 아침 식사 안 하심(화내시고 소리를 지르심)",
"박안순어르신 시름소리를 내셔서 자세를 좀 편안하게 눕혀드림",
"장현준 어르신 계속 손으로 침삼을 치며 소리 지르심",
"장현준어르신 식사 거의 못 드심",
"안경자어르신 바닥에 소변을 보심",
"손이순어르신 안 좋은 꿈을 꾸셨다며 거실에 나오셔서 한참우시고 기억이 나지 않는다며 한탄하심.",
"심상순어르신 수시로 바지 벗고 기저귀 빼버리고 시트에 소변을 보심",
"권계행어르신 계속 소리지르셔서 자세를 다시 잡아드림",
"윤준섭어르신 집에 간다고 자꾸 내려오려고 해서 침상칸막이 설치",
"이창석어르신 새벽에 나오셔서 수면유도해드림.",
"이창석어르신 아침에 뒷물하셨는데 잊어버리고 또 몇 번이나 화장실로 가셔서 찬물 바가지 들고 해야한다고 함",
"장현준어르신 밤새도록 똑똑거리며 침대난간을 두드렸어요.",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음"]

daily_6 = ["김영한어르신 계속 이를 갈아서 주변분 잠을 설침",
"김기애어르신 밤중에 손뼉치시네요.",
"정점순어르신 밤에 침상에서 앉아다 일어나기를 반복하시면서 새벽에 잠이듬",
"이흥열어르신 화장실간다고 자주 나오심",
"김영한어르신 침상에서 나오시려고 해서 침대칸막이를 했다가 아침에 제거함",
"양금식어르신 밤사이에 대변을 시트등에 묻혀나서 다 교체해드렸음",
"김영한어르신 밤새 이를 가심",
"최두영어르신 화장실 간다고 자주 나오심",
"변금준어르신 아침식사 안 하셔서 케어윌 한잔 드림",
"김소녀어르신 아침식사 안하셔서 케어윌 한잔드림",
"이흥열어르신 밤새 방안에서 배회하시면서 안 주무심",
"남춘녀어르신 사타구니에 발적보여서 연고 발라드림",
"김영한어르신 피부가려움에 힘들어하셔서 연고와 로션 발라드림",
"단명배어르신 등에 발적이 보여서 연고와 체위해드림",
"이세구어르신 계속 약달라고 조르심",
"김종운어르신 식사를 잘 못 하심",
"김종운어르신 변을 만져서 침상과 옷을 오염시켜서 교체 해드리려는데 어르신이 폭력을 행사함",
"김종남어르신 밤새 몇시냐고 밖으로 나오심",
"이흥열어르신 벽에 소변을 보시고 계속 화장실 드나드심",
"이세현어르신 계속 신음소리냄 (특별히 어디 불편한 것은 없어보임)",
"공월희어르신 L-tube 줄을 빼서 아침 못 드림",
"정점순어르신 소리지르며 알 수 없는 말씀을 하심",
"박안순어르신 시름소리를 내셔서 자세를 좀 편안하게 눕혀드림",
"공월희어르신 밤새 소리 지르심",
"최두영어르신 몇 차례 화장실 가신다고 밖으로 나와서 배회하셔서 취침 유도해 드림",
"김달산어르신 자꾸 손이 바지속으로 들어가서 옷이랑 시트를 다 오염시킴. 다 교체해 드림",
"김영한어르신 밤새 소리지르고 앉아서 주무시지 않았음",
"김소녀어르신 자꾸 헛소리 하심. (딸이 기다린다고 등)",
"이흥열어르신 02시부터 tv틀어 놓으심",
"김기애어르신 손뼉치심(여러번)",
"양금식어르신 소변을 이불에 다 싸서 이불 빨려고 내놓음. 그래도 방안에서 냄새가 많이나서 환기를 시킴",
"최두영어르신 화장실간다고 몇번 나오셔서 배회하셔서 모시고 들어감",
"양금식어르신 밤새 침대를 이리 저리로 옮기며 잘 주무시지 않으셨음",
"이흥열어르신 화상실간다고 몇차례 나오심 좌변기물을 떠다놓고 마심.",
"변금준어르신 밤중에 소리를 지르셨음. 그리고 금방 조용해지셨음",
"정점순어르신 새벽쯤에 나간다고 하셔서 침대난간을 침.",
"김영한어르신 가렵다고 하셔서 로션 발라드렸음",
"이흥열어르신 밤에 몇번 나오심",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음",
"이상없음"]


for i in range(1,4):
    browser.find_element_by_xpath(f"//*[@id='login_outline']/div[1]/div/form/ul/li[{i}]/input").send_keys(id[i-1])

browser.find_element_by_class_name("btn").click()

time.sleep(2)

# 팝업 창
pyautogui.click(pyautogui.locateOnScreen("mecro_img/close.png"))
time.sleep(0.1)
pyautogui.click(pyautogui.locateOnScreen("mecro_img/close.png"))
time.sleep(0.2)
# 왼쪽 6번 버튼
browser.find_element_by_xpath("//*[@id='left_area']/div[4]/ul/li[6]").click()
# 6번 세부버튼
browser.find_element_by_xpath("//*[@id='left_sub6']/div[2]/table/tbody/tr[2]/td/div/ul/li[3]").click()
time.sleep(0.5)




def do_text():
    time.sleep(1)
    pyautogui.scroll(400)
    time.sleep(0.5)

    rk = []
    rand_n = choice([0,1])

    # 5층
    for i in pyautogui.locateAllOnScreen("mecro_img/5floor.png", grayscale=True):
        rk.append(i)
    pyautogui.click(rk[rand_n])
    
    time.sleep(0.5)
    browser.find_element_by_xpath("//*[@id='tbl_manageDailyNight']/tbody/tr[21]/td[2]/textarea").click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyperclip.copy(choice(daily_5))
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)
    # 저장 버튼
    browser.find_element_by_class_name("btn_type1").click()
    time.sleep(0.3)

    pyautogui.scroll(400)
    time.sleep(0.5)
    
    rk = []
    rand_n = choice([0,1])

    # 6층
    for i in pyautogui.locateAllOnScreen("mecro_img/6floor.png", grayscale=True):
        rk.append(i)
    
    pyautogui.click(rk[rand_n])
    
    time.sleep(0.5)
    browser.find_element_by_xpath("//*[@id='tbl_manageDailyNight']/tbody/tr[21]/td[2]/textarea").click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyperclip.copy(choice(daily_6))
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)
    # 저장 버튼
    browser.find_element_by_class_name("btn_type1").click()
    time.sleep(0.5)
    # 취소 버튼
    browser.find_element_by_class_name("btn_type3").click()
    time.sleep(0.5)

def do_2(i):
    try:
        #이름 선택
        browser.find_element_by_xpath(f"//*[@id='daily_check_list']/table/tbody/tr[{i}]/td[3]").click()
        # //*[@id="daily_check_list"]/table/tbody/tr[1]/td[4]
        # //*[@id="daily_check_list"]/table/tbody/tr[2]/td[3]
        # //*[@id="daily_check_list"]/table/tbody/tr[3]/td[3]
        # //*[@id="daily_check_list"]/table/tbody/tr[4]/td[3]
        # //*[@id="daily_check_list"]/table/tbody/tr[5]/td[4]
        do_text()
    except:
        print("직접 수정",j,k)
        

def do_3(i):
    try:
        #이름 선택
        browser.find_element_by_xpath(f"//*[@id='daily_check_list']/table/tbody/tr[{i}]/td[4]").click()
        
        do_text()
    except:
        print("직접 수정",j,k)





start = 4  # 3월 첫 째 주 시작 갯수
T1 = [1,3,5,7,8,10,12]
T0 = [4,6,9,11]
T2 = [2]

for i in range(1,2):

    for j in range(1,13):

        if j in [7]:
            time.sleep(0.5)
            # 날짜 설정 버튼
            browser.find_element_by_class_name("s3").click()
            time.sleep(0.2)

            pyautogui.click(pyautogui.locateOnScreen("mecro_img/button.png"))
            time.sleep(0.1)

            # 년도 선택
            pyautogui.click(pyautogui.locateOnScreen(f"mecro_img/202{i}.png"))
            time.sleep(0.5)

            # 월 선택
            pyautogui.click(pyautogui.locateOnScreen(f"mecro_img/{j}m.png"))
            time.sleep(0.5)

# region=(1124,230,(1492-1124),(557-230)

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
                

