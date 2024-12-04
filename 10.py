#딕셔너리 ->되게 중요!!!
a = {} #dictionary
print(type(a))
b = {1} #set()
print(type(b))
c = dict()
c = {1: 'a', 'b' : 'b'}
print(c)
c[2] = 'c' #인덱스가 아니라 key
c['c'] = 2 #인덱스가 아니라 key
print(c)
del c[2]
del c['b']
print(c)

print(c.get(2))
print(c.keys())
print(c.values())

for i in c.keys() :
    print(i, c.get(i))

print('c' in c) #print('c' in c.keys())
print(2 in c.values())

#딕셔너리 응용
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic :
    print(f'{word}: {dic[word]}')
else :
    print("정의된 단어가 없습니다.")

#실습1. set 사용
# https://www.acmicpc.net/problem/14425
N, M = map(int, input().split())
S = set()
for i in range(N) :
    S.add(input())
ans = 0
for _ in range(M) :
    t = input()
    if t in S :
        ans+=1
print(ans)

#실습2. 딕셔너리 사용
score = dict()
score['Alice'] = 85
score['Bob'] = 90
score['charlie'] = 95

score['David'] = 80
score['Alice'] = 88

del(score['Bob'])
for i in score.keys() :
    print(i,score.get(i))