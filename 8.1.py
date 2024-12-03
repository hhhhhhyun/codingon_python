#리스트 평균 구하기
num = (input('숫자 여러 개 입력 >'))
listup=list(map(int, num.split()))
print(listup)
print('가장 큰 값:', max(listup))
print('가장 작은 값:', min(listup))
listup.remove(max(listup))
listup.remove(min(listup))
print('나머지 값의 평균: ',sum(listup)/len(listup))