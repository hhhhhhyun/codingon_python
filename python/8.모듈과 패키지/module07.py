#time.time() : 현재 시간을 실수 형태로 돌려주는 함수
import time

#2초후 루프 실행
print(time.time())
time.sleep(2)
print(time.time())
print()

a = time.time()
time.sleep(2)
b = time.time()
print(b-a)
print()

#time.localtime() : 연도, 월, 일, 시 ,분, 초 ...형태
print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)
print()

print(time.ctime()) #현재시간
print(time.ctime(a))
print(time.ctime(b))
print()

#1970년 1월 1일 기준
year = time.time()/(365*24*60*6) #년 -> 초 바꾸기
print(year)
day = time.time()/(24*60*60) #하루 -> 초 바꾸기
print(day)
print()

#수행시간 측정하기 #중요해!!
start = time.time()

for i in range(10) :
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간 : {end-start}초")
print()

#ㄴ함수로 바꾸기
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행시간 : {end-start}초")

def a():
    for i in range(10) :
        print(i)
        time.sleep(1)

def b():
    for i in range(100) :
        print(i)
        time.sleep(0.5)

#check_time(a)
check_time(b)