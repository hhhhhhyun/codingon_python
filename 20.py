#Lambda Expressions(람다식)
add = lambda x, y : x + y
print(type(add))
print(add(1, 2))

def add2(x, y):
    return x+y

add3 = add2
print(add2(1,2))
print(add3(1,2))

#람다 함수를 매개 변수로 전달하기
def call_3(func):
    for i in range(3):
        func()

call_3(lambda:print("hi"))
call_3(lambda:print("hello"))

#
def download(startedcallback, endedcallback):
    startedcallback()
    print("download중")
    endedcallback()

download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다."))

#lambda-bam() 함수와 함께 사용
list(map(int, ["1", "2", "3"]))

result = map(lambda x:3*x, [1,2,3,4])
print(list(result))

#lambda-filter() 함수와 함께 사용
li = [5, 1, 2, -11, 76]

value = list(filter(lambda x:x<0, li))
print(value) #[-5, 11]

value = list(filter(lambda x:x>10, li))
print(value) #[-5, 11]

#실습0. 2배 후 3이상인 것 출력
li = [5, 1, 2, -11, 76]

value = list(filter(lambda x:x>=3, map(lambda x:2*x, li)))
print(value)