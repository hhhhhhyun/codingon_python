#실습. 로또 번호 뽑기
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