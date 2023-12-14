#f = open("새파일.txt", 'a')
#f = open(r"c:\doit\a.txt", 'a', encoding="UTF-8") # r 문자(raw string) \경로
f = open("c:/doit/b.txt", 'a', encoding="UTF-8") # 일반경로
#lines = f.readlines() #readlines는 리스트로 넘겨줌
for i in range(11,13) :
    result= "이 문장은 %d번째 문장입니다.\n" % i
    f.write(result)
f.close()