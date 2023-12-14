#pyautogui

import pyautogui
import time

#pyautogui.moveTo(489,247,2)
#pyautogui.position() #현위치
#pyautogui.moveRel()  #현위치에서 상대위치 이동
#pyautogui.doubleClick() #더블 클릭
#pyautogui.click(clicks=2, interval=2) #클릭2회 2초간격
pyautogui.moveTo(1327,920,1)
pyautogui.doubleClick(button='right') #더블 클릭
#pyautogui.click(clicks=2) #클릭2회 더블클릭과 동일
time.sleep(2)
pyautogui.typewrite('hello world\n') #한글입력시 출력안됨
#pyautogui.typewrite(['a','b','c','enter']) #문자 abc입력후 엔터까지

