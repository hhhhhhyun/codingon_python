#재귀함수
#"Hello World!" 무한 출력
def hello():
    print("hello")
    hello()

hello()

#3번하고 종료하도록 출력
#return: 무한루프를 막아준다.
def hello() :
    global a
    if a == 3 :
        return 
    print("Hello World!")
    a += 1
    hello()

a = 0
hello()