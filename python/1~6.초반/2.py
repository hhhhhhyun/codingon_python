#<20241130>

#리스트와 조건문
a = []
b = [1,2,3,4]
c = ["장원영", "안유진"]
ㅇ = [1, "아이브"]

print(len(c)) #len() : 길이
print(c[0]) 
print(c[1])
print()

c[0] = "카리나"
print(c)
del c[0]
print(c)
print()

#
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])