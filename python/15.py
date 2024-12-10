#변수
def oneUp() :
    global x     # x = 0 을 의미함. global을 사용해야 작동!
    x = x + 1
    return x

x = 0          # = global x
print(oneUp())
print(oneUp())
print(oneUp())

#실습5. 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.
def get_times(n) :
    global count
    for i in range(1,31) :
        if i % n == 0 :
            count +=1
    return count

count = 0
n = 3

get_times(n)
print(f'\n({n}의 배수와 배수의 개수: {count})') #\n: 줄바꿈