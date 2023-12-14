
#1000미만의 자연수에서  
#3,5의 배수의 총합 
#입력 : 배수 2개, 자연수
#출력 : 배수의 총합 result


def multi (x, y, z) : 
    result=0
    for n in range(1,z) :
        if n % x ==0 or n%y ==0 :
            result += n
    print(result)
multi(4,5,100)