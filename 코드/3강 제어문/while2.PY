coffee = 3
money = 300
while money:
    print("돈을받았으니커피를줍니다.")
    coffee = coffee -1
    print("남은커피의양은%d개입니다." % coffee)
    if not coffee:
        print("커피가다떨어졌습니다. 판매를중지합니다.")
        break