#사번 자동부여
class Employee :
    serial_num = 1000

    def __init__(self, name) :
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self) :
        return f"사번 : {self.id}, 이름 : {self.name}"
    
e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]

print()

for i in employee:
    print(i)

print("\n". join(map(str, employee)))

print()
print()

#
print("hi", 'hello')
print("hi", 'hello', sep="")
print("hi", 'hello', end="")

print()

print(type("10"))
print("what's your name")
print("what's your \n name")
print("what's \t your name")
print()

#실습
print(f"빵의 개수: {30 // 4}")
print(f"남은 빵의 개수: {30 % 4}")
print()

print(f"빵의 개수: ", 30 // 4)
print(f"남은 빵의 개수: ", 30 % 4)
print()

a = input("1 + 1 = ?")
print(a)
print()

#
print("│ \_/ │")
print("│ q p │  /")
print("( 0 ), \"\"\"")
print("\^\"'     │")
print("││_/=\\_ _│")
print()
            
print(bin(10))
print(hex(10))
print()

print("!" * 10)
print()

python = '파이썬'
python * 3
#
#1번
