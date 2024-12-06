#<20241206>

#함수의 기본 매개변수
#기본 매개변수
def pr_str(txt, count=1, count2=1) :
    for i in range(count) :
        print(txt)
        print(count2)

pr_str("Hello", 3, 2)
pr_str("Hello", 3)
print()
pr_str("Hello")
print()

#가변 매개변수
def calc_avg(*numbers) : # *: 입력값을 여러 개 받을 수 있다. ex) calc_avg(1, 2, 3)
    #print(type(numbers))
    print(numbers)
    return sum(numbers) / len(numbers)

print(calc_avg(1,2))
print(calc_avg(1,2,3,4,5))

def a() :
    return 1,2

print(a())

#가변 키워드 매개변수
def intro(**kw) :
    print(type(kw))
    for k, v in kw.items() :
        print(f'{k}: {v}')
    for i in kw :
        print(f"{i}")

intro(name="Alice", age=25, city="NY")