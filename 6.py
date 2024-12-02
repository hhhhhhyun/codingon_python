print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." % (12,2))
print("오늘은 %d%s %d일 입니다." (12,'월',2))
print(f"오늘은 {12}{'월'} {2}일 입니다.")
print("오늘은 " +str(12)+"월"+str(2)+"일 입니다.")

print("Hello".upper())
print("Hello".lower())

friends = "고찬국 김다운 김민창"
a = friends.split("김")
print(a)

sentence = "{1}월 {0}일".format(12,2) # 12월 2일
print(sentence)

b = "  111  222  "
print(b.strip())
print(b.split())
# print(b.replace)

#실습2
a = input()
b = input()
print(int(a) * int(b[2]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a) * int(b))




