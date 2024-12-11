#파일 입출력
f = open("text.txt", "a") #"w" : 처음부터 새로 쓴다.
f.write('Hello World!!!!addaddff\n') #f.write의 반환값은 문자 길이
f.close() #꼭 닫아줘야함!, close하기 전엔 저장이 안됨

f2 = open("text.txt")
print(f2.read(2))
f2.close()

f3 = open("text.txt")
print(f3.readline(), end="")
print(f3.readline(), end="")
print(f3.readline(), end="")
f3.close()