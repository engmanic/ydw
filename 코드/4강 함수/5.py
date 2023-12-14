f = open("C:/doit/새파일.txt", 'a', encoding='utf-8')
#lines = f.read()
for i in range(1,3) :
    data='%d줄 입니다.\n' % i
    print(data)
    f.write(data)
f.close()