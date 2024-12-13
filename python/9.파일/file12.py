#raise 
a = 1
try:
    a +=1
    if a > 1:
        raise Exception #raise 사용시 반드시 Exception으로 빠진다. -> 강제로 에러 발생시키는 것
    a +=2
    print("a", a)
except:
    print("error", a)

#ㄴ예제
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    
    def cry(self):
        raise NotImplementedError
    
class Dog(Animal):
    def cry(self):
        print("멍멍")

d = Dog()
d.breathe()
d.cry()
        

