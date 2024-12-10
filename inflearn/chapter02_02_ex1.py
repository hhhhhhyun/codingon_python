#chapter02-1-ex1
#파이썬 완전 기초
#print 사용법
#파이선 3가지 print Formatting
#자주 나오는 질문 참고

"""
참고: Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
'''
"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text,  (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}' .format(n=n, s=text, sum=x+y) # format함수 쓸 때는 중괄호{}
print(ex2)

#출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

#rnqnsrlgh
m = 1000000000000000000

print(f'm : {m:,}')
print()
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20

print(f't : {t: ^10}')
print(f't center : {t: 10}')
print(f'center : {t: < 10}')
print(f't center : {t : > 10}')

n = 700
print(type(n))
print()

m = 800
n = 400
print(id(m),id(n))

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""