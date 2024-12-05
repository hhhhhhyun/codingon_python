#함수
def f(x) :
    result = x**2 +2*x + 1 #**: 제곱
    return result; 

print(f(3))

#-1
def sayHi() :
    print("Hi")
    print("Hi")
    print("Hi")

sayHi()

#-2
x = 10
def func2() :
    print("func2", x)

def func() :
    x = 20
    print("func", x)
    func2()

func()
print("main", x)

func2()

#-3
def func3(x) :
    print("func3", x)

func3(3)

#실습1. 두수(2,2)를 매개변수 전달하여 서로 같으면 곱하고, 서로 다르면 더하는 함수를 정의하고 호출하는프로그램을 작성하세요.
def f(x,y) :
    if x==y :
        print(f"결과(곱): {x*y}")
    else :
        print(f"결과(합): {x + y}")

f(2,2)
f(2,3)

#실습2. 
def price(x,y) :
    if x*y < 20000 :
        print(f"배송비 2,500원이 추가되어 총 {x*y +2500}원 입니다.")
    else :
        print(f"총 {x*y}원 입니다.")

price(30000,1)
price(17500,1)