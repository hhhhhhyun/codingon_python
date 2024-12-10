#실습3. 다음과 같은 조건을 만족하는 MinLimitCalculator 클래스 만들기
class Calculator :
    def __init__(self):
        self.value = 100
    
    def sub(self, value):
        self.value -= value

class MinLimitCalculator(Calculator) :
    def sub(self, value):
        self.value = max(0, self.value-value)
        #super().sub(value)
        #self.value = max(0, self.value) -> 복잡할 땐 이 코드 사용

cal = MinLimitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value) # 0 출력

