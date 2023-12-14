# 게시물의 총 개수와 한 페이지에 보여 줄 게시물 수를 입력
# 총 페이지 수를 출력
# 입력 : 게시물 수, 페이지당 게시물 수
# 출력 : 총 페이지 수

def get_page (x,y) :
    result=0
    if x % y == 0 :
        result = x//y
    else :
        result = x//y +1
    print(result)
get_page(100, 30)