
#1000미만의 자연수에서  
#3,5의 배수의 총합 
#입력 : 배수 2개, 자연수
#출력 : 배수의 총합 result


def multi (x, y, z) : 
    result=0
    n=1
    while n<z :
        if n % x ==0 or n%y ==0 :
            result += n
        n+=1
    return result
print(multi(2,3,100))