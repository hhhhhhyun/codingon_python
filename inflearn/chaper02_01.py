#기초문법

#print
print("hello")
print('hello')
print("""hello""")
print('''hello''')

#sep
print('h', 'e', 'l', 'l', 'o')
print('h', 'e', 'l', 'l', 'o', sep="   ")

#end
print('welcome to', end=' ')
print('inflearn', end=' ')
print()

#file 옵션
import sys #보라색: 예약어
print('learn', file=sys.stdout)
print()

# format 사용(d:3, s:'python', f:3.141592)
print('%s %s' % ('one', 'two')) # %s자리에 대체되어 들어갈 수 있음
print('{} {}'.format('one', 'two')) # {}와 함께 format함수를 사용함
print('{1} {0}'.format('one', 'two')) #코딩은 0부터 시작, 괄호안에 비어있을 땐 암묵적으로 {0} {1} 인것.

print()

# %s
print('%10s' % ('nice')) # 10개의 자릿수, 양수일 땐 왼쪽부터 공백으로 채움
print('{:>10}'.format('nice')) #왼쪽 기호일 땐 왼쪽부터~

print('%-10s' % ('nice')) # 10개의 자릿수, 음수일 땐 오른쪽부터 공백으로 채움
print('{:10}'.format('nice')) #부호 생략할 땐 오른쪽부터~

print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))

print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # . : 원하는 자릿수만큼 출력

print('{:10.5}'.format('pythonstudy')) #10개의 자리를 채우고 5글자만 출력(나머지 5개는 공백)

# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42)) # 문자열s에서는 s를 붙이지 않았지만 정수d 에서는 d를 붙여야한다.

# %f
print('%f' % (3.14123123123123))
print('%1.9f' % (3.14123123123123)) # 정수는 한자리, 소수점은 9자리까지 출력

print('{:f}' .format(3.14123123123123))

print('%06.2f' % (3.141592653)) # 정수부는 한자리이기 때문에 소수 2자리와 공백과 . 을 포함해 6자리 출력

#정리: 파이선 Format에는 %와 format함수가 있다!!ㅊ