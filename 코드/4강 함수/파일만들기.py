#f = open("c:/doit/새파일.txt", 'w', encoding="CP949")
f = open("새파일.txt", 'w', encoding="UTF-8")
for i in range(1,11) :
        result= "이 문장은 %d번째 문장입니다.\n" % i
        f.write(result)
f.close()
