#실습1. 회원 명부 작성하기
with open("member.txt", 'w') as f: #encoding="utf-8" : 한글 깨지지 않도록 출력하기 위해 인코딩을 해줘야함(or encoding = 'CP949')
    for i in range(3):
        text1 = input("이름을 입력하세요: ")
        text2 = input("비밀번호를 입력하세요: ")
        f.write(f"{text1} {text2} \n")

with open('member.txt', 'r') as f:
    print(f.read())

