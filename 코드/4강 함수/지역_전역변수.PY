a = [1,2,3]
result = a.append(4)
print(a)
print(result)

def vartest(a):
    a = a.append(5)
vartest(a)
print(a)

b= a.pop()
print(b)
print(a)

c=a.insert(0,10)
print(c)
print(a)

