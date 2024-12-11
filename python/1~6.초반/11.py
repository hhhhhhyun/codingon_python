#2차원 리스트
d = [
    [10,20],
    [30,40],
    [50,60]
]

print(d)
print(d[0][0]) # 0열0행
print(d[1][1]) # 1열1행
d.append([70,80]) # .append 함수: 요소 추가
print(d)
d[0][0] = 90
print(d)

d[1].pop() #pop은 마지막 숫자를 꺼내고 없애는 도구
print(d) 

print(len(d))
print(len(d[0]))

for i in range(0,len(d)) :
    for j in range(0,len(d[i])) :
        print(d[i][j], end=" ")
    print()

for x, y in d :
    print(x, y)