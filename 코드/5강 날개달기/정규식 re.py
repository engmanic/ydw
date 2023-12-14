import re
p=re.compile('[a-z]+')
m=p.finditer('life is too short')
for i in m : 
    print(i)
    print(i.group())
    print(i.span())
    
