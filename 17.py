#내장함수
list = [2,4,1,4,6]
list.sort() #원본변환
print (list)
list2 = [2,4,1,4,6]
print("sorted list2", sorted(list2)) #솔티드 된것만 변환
print("list2", list2)

# 오름 차순으로 정렬했을 때 3번째 값의 인덱스를 구하라
# 정렬하고 그 값을 원본에서 찾으면 된다

#함수 써서 정수 5 만들기
print(eval("1+2*2"))

#함수 안쓰고 정수로 만드는 방법: "0.5"를 더하라!
#코테에서 많이 쓰는 트릭임 
print(int(4.6 + 0.5)) #int는 내림을 해줌
print(int(4.4 + 0.5))

#그외 방법
print(round(4.5)) #round: 반올림
print(round(4.4))
print(round(4.6))

print(round(2.547))
print(round(2.547, 1))
print(round(2.547, 2))
print(round(127, -1)) # 1의자리 반올림
print(round(127, -2)) # 10의자리 반올림

#제곱구하기
print(2**3)
print(pow(2,3)) #pow(숫자, 몇제곱 할지)