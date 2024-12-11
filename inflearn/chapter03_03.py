#list
#시퀀스형
#자료구조에서 중요
#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#선언
a =[]
b = list()
c = [70, 75, 80, 85]
print(len(c))

d = [1000, 10000, 'Ace', 'Base'] #서로다른 자료형을 한 리스트 안에 넣을 수 있다.
e = [1000, 10000, ['Ace', 'Base','captain']] #리스트 안에 리스트 입력 가능
print(e)
print()

#인덱싱
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] +d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) # x[]: 리스트 값 출력
print('e - ', list(e[-1][1])) #list(): 리스트 형태로 출력
print()

#슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])
print()

#리스트 연산
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

#Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

#리스트 수정, 삭제 # c = [70, 75, 80, 85]
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] #삭제
print('c - ', c)
print()

#
print('a - ',a)