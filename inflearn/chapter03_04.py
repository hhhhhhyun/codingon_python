#튜플
#리스트와 튜플의 차이 비교 중요!!
#튜플 자료형(수정o, 중복o, 수정x, 삭제x) # 불변

#선언
a = () #튜플은 소괄호로 표현
b = (1, ) #원소가 하나일 땐 뒤에 콤마를 찍어줘야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

#인덱싱
print('d - ', d[0])
print('d - ', d[0] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) #리스트로 변환할 때 사용하는 방법
print()

#삭제x
#d[0] = 1500 -> 에러

#슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

#튜플 연산
print('c + d', c + d)
print()

#튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) #3은 인덱스에 몇번째야?
print('a - ', a.count(2))
print()

#팩킹, 언팩킹
#팩킹
t = ('foo', 'bar', 'baz', 'qux') #항상 쓰던 형태가 팩킹
print(t)
print(t[0])
print(t[-1])

#언팩킹
(x1, x2, x3, x4) = t #출력하면 괄호가 풀어져 있음, 입력 할 때 괄호 없이 x1, x2, x3, x4 = t 로 해도 출력O

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

#팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)