#<20241204>

#튜플(tuple)
t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0])
## del t1[0] 안됨
## t1[0] = 3 안됨
del t1

t2 = (10)
t3 = (10,)
t4 = 10, 20,
print(type(t4))

#셋(set)
set1 = {1,2,3,3}
print(set1)
set2 = set([2,3,4,4])
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0 :
    a = set2.pop()
    print(a)

set3 = set("apple")
print(set3)
while len(set3) > 0 :
    a = set3.pop()
    print(a)


name = ["1", "2", "3", "2"]

for i in range(len(name)) :
    if name.count(name[i]) > 1 :
        print(name[i])

name_set = set(name)
print(name_set)
name_list = list(name_set)
name_list.sort()
print(name_list)

#실습0 for루프 이용해서 중복 제거하기
name = ["1", "2", "3", "2"]
a = []
for i in range(len(name)) :
    if a.count(name[i]) < 1 :
        a.append(name[i])
name = a
print(name)
