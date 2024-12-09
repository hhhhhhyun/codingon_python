class MyAdd :
    __a = 1
    __b = 2

    def sum(self):
        return self .__a + self .__b
    def set_a(self, a):
        self.__a = a

a = MyAdd()
print(a.sum())
a.set_a(3)
print(a.sum())