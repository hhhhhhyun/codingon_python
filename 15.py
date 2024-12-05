#변수
def oneUp() :
    x = 0     #전역변수 는 global로 쓸수있다. ex) global x
    x = x + 1
    return x

x = 0          # = global x
print(oneUp())
print(oneUp())
print(oneUp())

#실습5. 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.
def 