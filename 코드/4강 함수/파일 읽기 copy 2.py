#f = open("c:/doit/새파일.txt", 'r')
f = open("c:/doit/새파일.txt", 'r', encoding="UTF-8")
#lines = f.readlines() #readlines는 리스트로 넘겨줌
for line in f :  #파일에서 바로 읽기
    line=line.strip() #특수문자 제거
    if not line :
       break
    print(line)
f.close()