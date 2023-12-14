#특정 디렉터리부터 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)만 출력
#입력 : 디렉토리
#출력 : 파이썬 파일 리스트

# C:/doit/sub_dir_search.py
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError:
        pass

search('./')