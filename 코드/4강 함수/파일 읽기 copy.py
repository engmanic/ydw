#f = open("c:/doit/새파일.txt", 'r')
f = open("c:/doit/새파일.txt", 'r', encoding="UTF-8")
lines = f.readlines() #readlines는 리스트로 넘겨줌
for line in lines :
    #line=line.strip()
    line=line.replace('\n','')
    if not line :
       break
    print(line)
f.close()