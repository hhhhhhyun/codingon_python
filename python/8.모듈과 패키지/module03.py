# ㄴ확장: 10번 반복하면서 점수 계산하기(예: 3회-80점)
import random

com = random.randint(1,100)
score = 110
min_v = 1
max_v = 100
count = 0

while True :
    try:
        count += 1
        score -= 10
        guess = int(input("숫자 입력(%d - %d): " % (min_v, max_v)))

        if guess < 0 or guess > 100 :
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            print(f"정답: {com}")
            print(f"점수: {score}")
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
            count += 1
            score -= 10
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")
