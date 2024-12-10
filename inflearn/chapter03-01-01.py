#형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

#형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) #True : 1, False : 0
print(float(False))
print(complex(3))
print(complex("3")) # 문자형->숫자형으로 자동으로 바꾼것
print(complex(False))
print()

print(abs(-7))
print()

x, y =divmod(100, 8)
print(x, y)
print(pow(5, 3))

#외부 모듈
import math

print(math.ceil(5.1))
print(math.pi)



