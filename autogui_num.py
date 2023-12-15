#pyautogui 이미지에서 계산기 숫자 위치 찾기 
#프로그래머 김플 스튜디오

import pyautogui
import time

#print(pyautogui.position()) #현위치 출력
#pyautogui.moveTo(838,130)
#pyautogui.click(838,130) 

# print(pyautogui.position())  #마우스 위치의 값7  찾기
# i= pyautogui.locateOnScreen('7.png') #Box(left=378, top=446, width=98, height=54)
# print(i)
# q= pyautogui.center(i) #i좌표의 중심값 구하기 Point(x=508, y=298)
# print(q)
# pyautogui.click(q)

# i= pyautogui.locateCenterOnScreen('7.png') #한번에 중심값까지 구하기 Point(x=508, y=298)
# print(i)
# pyautogui.click(i)

print(pyautogui.position())  #마우스 위치의 값1  찾기
pyautogui.screenshot('1.png',region=(508,391,30,30)) #스크린샷으로 1번 위치 저장 30*30픽셀
num1= pyautogui.locateCenterOnScreen('1.png') #한번에 중심값까지 구하기 
print(num1)
pyautogui.click(num1)

# pyautogui.click(num0)
# pyautogui.click(num1)
# pyautogui.click(num2)
# pyautogui.click(num3)
# pyautogui.click(num4)
# pyautogui.click(num5)
# pyautogui.click(num6)
# pyautogui.click(num7)
# pyautogui.click(num8)
# pyautogui.click(num9)


#pip install opencv-python        #이미지에서 위치 찾기
#pyautogui.moveTo(489,247,2)
#pyautogui.position() #현위치
#pyautogui.moveRel()  #현위치에서 상대위치 이동
#pyautogui.doubleClick() #더블 클릭
#pyautogui.click(clicks=2, interval=2) #클릭2회 2초간격
# pyautogui.moveTo(1327,920,1)
# pyautogui.doubleClick(button='right') #더블 클릭
#pyautogui.click(clicks=2) #클릭2회 더블클릭과 동일
# time.sleep(2)
# pyautogui.typewrite('hello world\n') #한글입력시 출력안됨
#pyautogui.typewrite(['a','b','c','enter']) #문자 abc입력후 엔터까지

