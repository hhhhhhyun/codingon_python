#<20241203>
#반복문
i=0
while i<5 :
    i +=1
    print(i)
print("끝")

#실습0:1~10사이 홀수만 출력
num = 0
while num < 10 :
    num += 1
    if num % 2 != 1 :
        continue
    print(num)

#for문
#실습1: 1부터 사용자가 입력한 수까지 정수의 합 계산
num=int(input("어디까지 계산할까요?"))
sum_val = 0
for i in range(1,num+1) :
    sum_val += i
print(f"\n합계 {sum_val}")

#실습2 입력한 숫자만큼 카운트하고 "발사" 출력
num=int(input("몇초?: "))
for i in range(num,0,-1) :
    print(i,end=" ") # end=" "줄을 바꾸지 않고 스페이스만 출력하라는 의미
print("발사!!")

#실습3 구구단 만들기 - 사용자가 입력한 숫자의 구구단 출력(for문의 단골문제!!)
a = int(input("몇 단을 출력할까요?: "))

for i in range(1, 10) :
    print(f"{a} * {i} = {a*i}") 

#for문 - 리스트
a = [10, 20, 30]
print(sum(a))
sum=0
for i in a:
    sum += i
print(sum)

a = [1,2,3,4,5]
a2=[]
a3=[]
a4=[]

a3 = [i*3 for i in a]
print(a3)

a4 = [i*3 for i in a if i%2==0]
print(a4)

#이중 for문
for y in range(3) :
    for x in range(2) :
        print(f"y: {y}, x: {x}")
    print()

for i in range(2,10) :
    print(f'[{i}단]')
    for j in range(1,10) :
        print(f'{i} * {j} = {i*j}')
    print()

#자리배치도
print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1

for i in range(0, row):
    for j in range(1, column + 1):
       seat = i * column + j
       if seat > customer:
          break
       print(seat, end=" ")
    print()

#실습4 별 찍기
star = int(input('몇줄?: '))
for i in range(1,11) :
    for j in range(i) :
        print("*", end ='')
    print()

star = int(input('몇줄?: '))
for i in range(1,6) :
    print(" " * (star-i) + "*" * i)

star = int(input("몇줄?: "))
for i in range(1,6) :
    print(" " * (star-i) + "*" * (2 * i -1))

#실습5 리스트 평균 구하기
num = (input('숫자 여러 개 입력 >'))
listup=list(map(int, num.split())) #!!외우기!!: c = list(map(int, input().split()))
print(listup)
print('가장 큰 값:', max(listup))
print('가장 작은 값:', min(listup))
listup.remove(max(listup))
listup.remove(min(listup))
print('나머지 값의 평균: ',sum(listup)/len(listup))