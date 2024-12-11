#실습. 영어타자 연습 프로그램
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'grape', 'garlic', 'onion', 'potato']
n = 1 #문제번호

input("[타자게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question)
    user = input()
    if question == user :
        print("통과!!")
        n += 1
    else:
        print("오타! 다시도전!")

end = time.time() # 종료 시간
et = end - start

print(f'타자시간: {et: .2f} 초') #실수를 소수점 2개 자리 까지 표시
