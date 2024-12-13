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
c[0] = 4 #첫번째를 4로 바꾼다
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] 
print('c - ', c)
c[1] = ['a', 'b', 'c'] #리스트 형태로 삽입
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] #인덱스의 2번째 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1,4]
print('a - ',a)

a.append(10) #끝에 추가
print('a - ', a)
a.sort() #오름차순 정렬
print('a - ', a)
a.reverse() #거꾸로 뒤집어서 정렬
print('a - ', a)
print('a - ', a.index(3), a[3]) #a.index(3): 인덱스에서 3은 몇번째에 있어?
a.insert(2,7) #인덱스의 2번째 자리에 7을 넣어~
print('a - ', a)
a.remove(10) #10을 지워줘!
print('a - ', a)
print()

print('a - ', a.pop()) #a.pop(): 마지막에 있는 원소를 가져오고 지워줌
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) #a.count(4): 리스트에 4는 1개 있다
print()

ex = [8, 9]
a.extend(ex) #현재 리스트 끝에 ex리스트 원소들을 붙여넣을게~
print('a - ', a)

#삭제: remove, pop, del 세가지 많이 쓴다.

#반복문 활용
while a:
    data = a.pop()
    print(data) #끝에서 원소를 하나씩 계속 꺼내오다가 리스트가 비어지면 반복문이 끝남
