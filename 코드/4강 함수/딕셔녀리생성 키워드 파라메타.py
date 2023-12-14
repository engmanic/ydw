def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs['name'])
#for k in kwargs.keys():
#if(k=="name"):

print_kwargs(name='foo', age=3) #딕서너리 형태로 데이터 생성
