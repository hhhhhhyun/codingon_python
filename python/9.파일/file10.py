#실습. 정수 입력 받기
#사용자가 제대로 된 정수를 입력할 때까지 반복하여 입력 받기
while True:

    try:
        num = int(input('정수를 입력하세요: '))
        print("예외없음!성공적!!")
        break
    except ValueError:
        print("존재하지 않는 변수 호출")


