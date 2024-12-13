#에러와 예외
# 예외처리

#방법1
try : #에러가 날 것 같은 곳을 미리 처리해두기
    num = int(input("정수입력"))
except ValueError:
    print('정수가 아님!')

#방법2. 에러가 난 곳을 메시지로 알려줘
try :
    num = int(input("정수입력"))
except ValueError as msg:
    print(msg)

#방법3. #ValueError 안써도 출력
try :
    num = int(input("정수입력"))
except :
    print('정수가 아님!')

#Exception 사용하기

try :
    num = int(input("정수입력: "))
except Exception as msg:
    print(msg)

#에러 발생 즉시 점프해서 출력
try :
    num = int(input("정수입력: "))
except Exception as msg:
    print(msg)
else:
    print("예외없음")

#에러 처리 순서
try :
    num = int(input("정수입력: "))
except Exception as msg: # Exception값을 먼저 출력
    print("Excetion", msg)
except ValueError as msg:
    print("Excetion", msg)
else:
    print("예외없음")
'''
모두 에러가 날 땐 먼저 입력한 값을 먼저 출력한다.
따라서, 먼저 큰 값들을 처리해주는 예외처리를 순서대로
입력해주는 것이 좋다.
'''