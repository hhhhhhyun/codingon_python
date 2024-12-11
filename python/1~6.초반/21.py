#<20241207>

#복습
#함수안에 함수를 쓸 수 있다.
def b() :
    def c() :
        print("c")
    c()

b()

#list를 문자로 바꾸는 것
l = ["p", "y", "t", "h", "o", "n"]
print("" .join(l))

# map
# map은 그대로 쓸 수 없기 때문에 list 등등으로 변환하여 사용한다.
print(list(map(lambda x : 3*x, [1,2,3,4])))

print(list(map(int, input() .split())))
