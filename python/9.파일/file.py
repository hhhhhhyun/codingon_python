f = open("./text.txt", "a") #"w" : 처음부터 새로 쓴다.
f.write('Hello World!!!!addadd \n') #f.write의 반환값은 문자 길이
f.close()

f2 = open("./text.txt")
print(f2.read(2))
f2.close()