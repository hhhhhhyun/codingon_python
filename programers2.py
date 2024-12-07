#프로그래머스 스쿨
#코딩테스트 연습 > 연습묹 > 나누어 떨어지는 숫자 배열
# (ex1. array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요. 
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.)
def solution(arr, divisor):
    answer = []
    for i in arr :
        if i %  divisor == 0 :
            answer.append(i)
            answer.sort()
    if len(answer) == 0 : #len(answer)의 의미: 리스트가 비어 있는지 확인하는 일반적인 방법. 비어 있는 리스트의 길이는 0 이므로 len(answer) == 0
        answer .append(-1)
    
    return answer

#
print(1 if 1<0 else 0) #많이 쓰는 구문!
print("abc" if 1<0 else "bcd") #아래의 if문을 한줄로 바꾼 것

if 1<0 :
    print("abc")
else :
    print("abc")

#코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기
# (ex2.정수 배열 numbers가 주어집니다. 
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.)
def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) : #j는 언제나 i다음의 수
            answer .append(numbers[i]+numbers[j])
    answer = sorted(set(answer)) #
    
    return answer

# 코딩테스트 > 연습문제 > 하샤드 수
#(ex3. 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.)
def solution(x) :
    s = str(x)
    sum = 0
    for i in s :
        sum += int(i)
    
    return x % sum == 0

#코딩테스트 연습 > 연습 > 문자열 내림차순으로 배치하기
#(ex4.문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, 
# solution을 완성해주세요.
#s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.)
def solution(s)    #아스키코드 상에서는 대문자가 소문자보다 작다.
    answer = ''
    ls = list(S)
    ls.sort(reverse = True)

    print(ls)
    return '' .join(ls)
#best answer
def solution(s) :
    return '' .join(sorted(s, reverse=True))

#코딩테스트 연습 > 연습문제 > 추억점수
#(ex5.사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 
# 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다. 
# 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 
# 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다. 
# 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고, 
# "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.
# 그리워하는 사람의 이름을 담은 문자열 배열 name, 
# 각 사람별 그리움 점수를 담은 정수 배열 yearning, 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.)
def solution(name, yearning, photo) :
    answer = []
    d = {}
    for i in range(len(name)) :
        d[name[i]] = yearning[i]

    for i in photo :
        sum = 0
        for j in i :
            v = d.get(j)
            if v :
                sum += v
            answer .append(sum)
    return answer

