##ㄴ예제
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    
    def cry(self):
        raise NotImplementedError #raise NotImplementedError 대신 raise Exception을 사용해도 된다.
    
class Dog(Animal):
    def cry(self):
        print("멍멍")

d = Dog()
d.breathe()
d.cry()

