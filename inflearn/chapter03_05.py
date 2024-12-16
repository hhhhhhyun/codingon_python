#딕셔너리
#범용적으로 가장 많이 사용
#딕셔너리 자료형(순서x, 키 반복x, 수정o, 삭제o)

#선언 #여러가지 선언 방식이 있음
a = {'name' : 'Kim', 'phone' : '010123123123', 'birth' : '988494958'} #Kim을 찾기 위해 name이라는 키가 필요함
b = {0 : 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {                     # d : 일반적인 딕셔너리 형태의 입력
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Niceman',
    City='seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a - ', type(a),a)
print('b - ', type(b),b)
print('c - ', type(c),c)
print('d - ', type(d),d)
print('e - ', type(e),e)
print('f - ', type(f),f)

#출력
print('a - ', a['name']) #존재x -> 에러발생
print('a - ', a.get('name')) #존재x -> None처리, 에러 발생시 None이라고 표시되어 프로그램의 흐름이 끊기지 않아 get함수를 더 많이 사용함
print('b - ', b[0])
print('f - ', f.get('City'))
print('f - ', f.get('Age'))