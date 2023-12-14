# 문서 파일 안에 있는 탭 문자(Tab)를 공백 문자(Space) 4개로 바꾸어 
# python tabto4.py src dst
#입력 : 문서파일
#출력 : 수정파일

import sys
src=sys.argv[1]
dst=sys.argv[2]

f=open(src)
tab=f.read()
f.close()

space=tab.replace('\t',' '*4)

f=open(dst,'a')
f.write(space)
f.close()
print(space)


print(src)
print(dst)