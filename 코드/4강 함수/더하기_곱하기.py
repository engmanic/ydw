def add_mul(choice, *args) :
    if choice =="add" :
        result =0
        for i in args :
            result +=i
        return result
    elif choice =="mul" :
        result =1
        for i in args :
            result *=i
        return result
    else : print("add or mul")
#a= add_multiple(input(),1,2,3)
#print(a)