#표준 모듈-random 모듈
import random

print(random.randint(1,5)) # a~b까지 임의의 정수 리턴
print(random.uniform(1,5)) # a~b까지 임의의 실수 리턴
print(random.random()) # 0~1사이 임이의 실수 리턴
print(random.randrange(1,5)) # a~b까지 임이의 정수 리턴
print(random.randrange(1,5,2)) # randrange(a,b,step): step만큼 지정된 간격으로 임의의 정수 리턴

#실습.up_and_down 게임(숫자를 추측해서 맞히는 게임)
import random

com = random.randint(1, 100)
min_v = 1
max_v = 100

while True :
    try:
        guess = int(input("숫자 입력(%d - %d): " % (min_v, max_v)))

        if guess < 0 or guess > 100 :
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")



