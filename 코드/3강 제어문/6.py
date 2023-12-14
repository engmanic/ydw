a = [1,2,3]
b = a[::]
c = a.copy()

print(id(a),id(b), id(c))