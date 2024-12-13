#실습3. ㄴ로그인 성공 시 전화번호 저장하기
import sys

def successLogin(name, pw):
    dictUser = {}
    with open("member.txt", 'r') as f:
        for line in f:
            n, p = line.split()
            dictUser[n] = p

    print(dictUser)

    return pw == dictUser.get(name)
    
name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")
    
if not successLogin(name, pw):
    print("로그인 실패")
    sys.exit(0)

print("로그인 성공")
phone = input("전화번호를 입력하세요.: ")

with open("member.txt", "r") as f:
    m_tel_list = f.readlines()
    print(m_tel_list)

user_tel = name + " " + phone + "\n"

with open("member.txt", "w") as f:
    write = False
    for i in m_tel_list:
        if i.split()[0] == name:
            f.write(user_tel)
            write = True
        else :
            f.write(i)
    if not write:
        print("not write", user_tel)
        f.write(user_tel)
            

    
    
