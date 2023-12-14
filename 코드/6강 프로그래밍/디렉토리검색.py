#특정 디렉터리부터 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)만 출력
#입력 : 디렉토리
#출력 : 파이썬 파일 리스트

import os

def search(dirname) :
    try:
        for (path, dir, files) in os.walk(dirname):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.py':
                    print("%s/%s" % (path, filename))
    except PermissionError :
        pass

search('./')