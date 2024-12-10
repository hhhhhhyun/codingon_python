#정보은닉
class Health :
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getName(self):
        return self.__name
    
    def setHp(self, hp) :
        hp = max(hp, 0)
        hp = min(hp, 100)
        self.__hp = hp 

    def get_hp(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.setHp(self.__hp + hours)
        print(f"{hours}시간 운동하다")

    def drink(self, cups):
        self.setHp(self.__hp + cups)
        print(f"술을 {cups}잔 마시다")

p1 = Health("나몸짱")
p1.setHp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.getName()} - {p1.get_hp()}")

p2 = Health("나약해")
p2.setHp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.getName()} - {p2.get_hp()}")
