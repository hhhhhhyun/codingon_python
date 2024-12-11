#파이썬 문자형!!
#문자열 생성
str1 = " I am Python"
print(type(str1))
print()

#빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

#이스케이프 문자 사용
print('I\'m boy')

print('a \t b')
print('a \"\" b')
print()

#탭, 줄 바꿈

#Row String
raw_s = r'D:\python\test' #Row String(r)이 붙어 있으면 역슬래시(\)를 있는 그대로 표현할 수 있게 된다.
print(raw_s)

#멀티라인 입력 #역슬래시 사용해서 긴문장 보기좋게 나열
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)

multi_str1 = \
'String\n'\
'Multi line\n'\
'Test'

print(multi_str1)
print()

#문자열 연산
str_01 = "Python"
str_02 = "Apple"

print(str_01 * 3)
print(str_01 + str_02)
print('y' in str_01) #y가 str_01에 있니? -> True, False로 대답함
print()

#문자열 형 변환 (str()에 넣으면 문자열로 형 변환 해준다)
print(str(66), type(str(66)))
print(str(True),type(str(True)))
print()

#문자열 함수
print("Campitalize: ", str_01.capitalize()) #앞글자를 대문자로 반환
print("endswith: ", str_02.endswith("e")) #마지막 글자가 e로 끝나는가?
print("sorted: ", sorted(str_01)) #문자열을 리스트 형태로 반환
print("split: ", str_02.split('p')) #p를 기준으로 분리한다

#반복(시퀀스)
im_str = "Good boy!"

print(dir(im_str)) #__iter__

#출력
for i in im_str:
    print(i)

print()

#슬라이싱
str_s1 = "Nice Python"

#슬라이싱 연습
print(str_s1[0:3]) #0부터 (n-1)번째까지 출력
print(str_s1[5:]) #[5:11]
print(str_s1[:len(str_s1)]) #str_s1[:11]
print(str_s1[1:9:2]) #2번씩 건너뛰어서 [1:9] 출력
print(str_s1[-5:])
print(str_s1[1:-2]) 
print(str_s1[::2]) #[0:11:2]
print(str_s1[::-1]) #거꾸로 출력 -> [0:11:-1] 오른쪽에서 왼쪽으로 거꾸로 출력
print()

#아스키 코드
a = 'z'

print(ord(a)) #ord: 알파벳을 아스키코드로 -> z의 아스키코드 값으로 보여주는 함수
print(chr(122)) #chr: 아스키코드를 알파벳으로-> 아스키코드를 알파벳으로 보여주는 함수
