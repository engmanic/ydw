f=open("new.txt","w", encoding='utf-8')
while True:
    data = input()
    if not data: break
    print(data)
    f.write(data)
f.close()    