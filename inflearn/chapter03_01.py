#숫자형

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린(true, false)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

str1 = "Python"
bool = True
str2 = 'Anaconda'
float = 10.0 
list = [str1, str2] #list : [] 사용
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
} #dict={입력해야하는 값 : 찾고자하는 값}, ex) 2.0을 찾기 위해선 version을 입력해야한다.
tuple = (5,6,7) #tuple: () 사용 (괄호 없이 콤마로만 사용가능)
set = {2,3,4} #set : {} 사용

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y제곱 (= x**y)
"""






