#실습2. 회원 명부를 이용한 로그인 기능
'''
r: 파일을 읽기 위해서 연다(기본값)
w: 파일에 데이터를 쓰기 위해서 연다
a: 파일의 뒷부분에 데이터를 추가하기 위해 파일을 연다
'''
text3 = input(f'이름을 입력하세요: ')
text4 = input(f'비밀번호를 입력하세요: ')

with open('member.txt', 'r') as f:
    for check in f :
        n, p = check.split()

        if n == text3 and p == text4:
            print("로그인 성공")
        else :
            print("로그인 실패")
    

