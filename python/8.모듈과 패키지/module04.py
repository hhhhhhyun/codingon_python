#실습. 로또 번호 뽑기
# my
import random

num = []

for i in range(6):
    while True:
        i = random.randint(1,45)
        if i not in num:
            num.append(i)
            break
    
num.sort()
print(num)
#방법1
lotto = []
while len(lotto) < 6 :
    num = random.randint(1,45)
    if num in lotto :
        continue
    lotto.append(num)
    
print(sorted(lotto))

#방법2
#set(집합)으로 구현하기
lotto=set() 
while True:
    x= random.randint(1,45)
    lotto.add(x)
    if len(lotto) == 6:
        break
sorted_lotto = sorted(lotto)
print(sorted_lotto) #set은 sort() dksehla, sorted() 이용해서 새로운 리스트로

#방법3
lotto = random.sample(range(1,46), 6)
print(sorted(lotto))