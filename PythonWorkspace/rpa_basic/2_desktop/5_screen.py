import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장


# pyautogui.mouseInfo()
# 28,18 60,169,242 #3CA9F2

pixel = pyautogui.pixel(28, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(28, 18, (46,162,241)))
print(pyautogui.pixelMatchesColor(28, 18, pixel))
print(pyautogui.pixelMatchesColor(28, 18, (46,162,242)))

