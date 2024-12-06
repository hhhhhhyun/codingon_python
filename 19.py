#팩토리얼 구하기
def factorial(n) :
    if n == 1: 
        return 1
    return n * factorial (n-1)

print(factorial(5))

#실습2. 재귀 함수로 피보타치 수 구하기
#Fn = F(n-1) + F(n-2)
#방법1.
def fibo(n) :
    if n <= 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(1)) # '100'값을 넣으면 오래걸린다.

#방법2. 100값 빠르게 구하기!
memory = {1: 1, 2:1}

def fibo_memoization(n) :
    if n in memory:
        number = memory[n]
    else:
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number
    return number

print(fibo_memoization(100))

#재귀 유명한 문제,, 하노이의 탑,,
#Fn = F(n-1) + 1 + F(n-1)
def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)
