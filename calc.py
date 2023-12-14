class FourCal :
    def __init__(self,first,second) :
        self.first = first
        self.second = second
    def setdata(self,first,second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result
    def pow(self) :
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a=FourCal(2,0)
b=FourCal(3,4)
c=SafeFourCal(2,0)

print(a.div())
print(c.div())

#print(b.first)


