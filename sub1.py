#과제2. 자판기 프로그램
vending_machine = [ '게토레이', '레쓰비', '생수', '이프로']
beverage = input("마시고 싶은 음료?: ")

if beverage in vending_machine :
    print(f"{beverage}드릴게요")
else :
    print(f"{beverage}는 지금 없네요")

#과제3. 자판기 프로그램 응용
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
user = input("사용자는 '소비자' or '주인': ")

if user == '소비자' :
    choice = input("원하는 음료를 말해주세요.: ")
    if choice in vending_machine :
        vending_machine.remove(choice)
        print(f"{choice} 드릴게요.")
    else :
        print(f"{choice} 음료 없음")
elif user == '주인' :
    select = input("'추가' or '삭제': ")
    if select == '추가' :
        new_choice = input("추가할 음료를 입력하세요: ")
        vending_machine.append(new_choice)
        vending_machine.sort()
        print(f"현재 음료 리스트: {vending_machine}")
    elif select == '삭제' :
        delet_choice = input("삭제할 음료수를 입력하세요: ")
        if delet_choice in vending_machine :
           vending_machine.remove(delet_choice)
           print(f"{delet_choice}음료 제거완료. 현재 음료 리스트: {vending_machine}")
        else :
           print(f"{delet_choice} 음료 없음")
    else :
        print("잘못된 값을 입력하셨습니다. 다시 입력해주세요. ")
else :
    print("잘못된 값을 입력 하셨습니다. 다시 입력해주세요.")
    