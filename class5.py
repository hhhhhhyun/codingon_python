#실습1. 사칙연산 클래스 만들기
#조건)
#-인스턴스를 생성할 때 2개의 숫자를 class에 보낸다.
#-add 메서드는 두 수를 더한 결과값을 반환한다.
#-sub 메서드는 두 수를 뺀 결과값을 반환한다.
#-mul 메서드는 두 수를 곱한 결과값은 반환다.
#-div 메서드는 두 수를 나눈 결과값을 반환한다.
class calculation : 
    def __init__(self, a, b) :
        self.__a = a
        self.__b = b

    def add(self) :
        return self.__a + self.__b
    def sub(self) :
        return self.__a - self.__b
    def mul(self) :
        return self.__a * self.__b
    def div(self) :
        if self.__b == 0 :
            return None
        else :
            return self.__a / self.__b

n = calculation (3,2)
print(n.add())
print(n.sub())
print(n.mul())
print(n.div())