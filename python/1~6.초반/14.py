#매개변수로 리스트(배열) 전달
def times(a) :
    a2 = [i * 3 for i in a]
    return a2

v2 = times([1,2,3,4,5])
print(v2)

#실습3
vending_machine = ['게토레이', '게토레이', '레쓰비', '생수', '이프로']

def check_machine():
    print("남은 음료수: ", vending_machine)

def is_drink(vending_machine, drink):
    return drink in vending_machine

def add_drink(vending_machine, drink):
    vending_machine.append(drink)
    vending_machine.sort()

def remove_drink(vending_machine, drink):
    vending_machine.remove(drink)

while(1):
    who = int(input("사용자 종류를 입력하세요(1.소비자, 2.주인) : "))
    if who == 1:
        drink = input("마시고 싶은 음료? ")
        if is_drink(vending_machine, drink):
            print(drink, "드릴게요")
            remove_drink(vending_machine, drink)
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    else:
        todo = int(input("할 일 선택(1.추가, 2.삭제) : "))
        if todo == 1:
            print("남은 음료수: ", vending_machine)
            drink = input("추가할 음료수? ")
            add_drink(vending_machine, drink)
            print("추가 완료")
            print("남은 음료수: ", vending_machine)
        else:
            print("남은 음료수: ", vending_machine)
            drink = input("삭제할 음료수? ")
            if is_drink(vending_machine, drink):
                remove_drink(vending_machine, drink)
                print("삭제 완료")
                print("남은 음료수: ", vending_machine)
            else:
                print(f"{drink}는 지금 없네요")