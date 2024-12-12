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

#<20241212>
#파일
#readlines 
f4 = open('text.txt')
print(f4.readlines()) #readlines: 파일의 모든 줄을 읽음
f4.close()
print()

#seek
f5 = open('text.txt',"r+")
print(f5.read())
print(f5.tell()) 
f5.seek(4) #커서를 제일 앞으로 이동
print(f5.write("8"))
f5.close()
print()

#find함수로 찾을 수도 있음
f6 = open('text.txt',"r+")
str6 = f6.read()
print(f6.tell()) 
f6.seek(str6.find("5")) #커서를 제일 앞으로 이동
print(f6.write("8"))
f6.close()
print()

#with ~as 구문
#지원누수 방지를 돕는 with~as 구문
with open('text.txt',"r+") as f7:
    str6 = f7.read() 
    print(f7.tell()) 
    f7.seek(str6.find("4")) 
    f7.close()
    
print()


