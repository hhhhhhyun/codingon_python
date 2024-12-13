#finally, continue 함수
while True:

    try:
        num = int(input('정수를 입력하세요: '))
        print("예외없음!성공적!!")
        break 
    except ValueError:
        print("존재하지 않는 변수 호출")
        continue #try-except 구문을 벗어날 때 항상 실행
    finally: #맞든지 틀리든지 반드시 실행됨
        print("무조건무조건이야야")
