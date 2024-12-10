print(1 == 2)

x=2
print (1<x<3) 
print(True and False)
print(True or False)
print(not True)
# print(!True)

cart = ["계란", "마늘", "콩나물", "커피"]
print("두부" in cart)
print("계란" in cart)

if 1<3:
    print("True")
    print("True")
else:
    print("False")

#실습3
a = int(input())
if a % 2 == 0:
    print("짝수")
if a % 2 == 1:
    print("홀수")

#실습4
a = int(input("점수: "))
if a >= 90 : # >= 보다 < 한번만 비교하는게 더 효율적, ex) a > 89
    print("A")
if 80 <= a < 90 :
    print("B")
if 70 <= a < 80 :
    print("C")
if 60 <= a < 70 :
    print("D")
if a < 60 :
    print("E")

#실습5
age = int(input("나이를 숫자로 입력해주세요: "))
pay = input("결제 방법을 입력해주세요. ('카드' 또는 '현금'만 입력): ")

if age < 8 or age > 75 :
    fare = "무료"
if age < 14 :
    fare = 450
elif age < 20 :
    if pay == "카드" :
       fare = 720
elif age < 75 :
    if pay == "카드" :
       fare = 1200
    else :
        fare = 1300

        print(f"{age}세의 {pay}요금은 {fare}원 입니다.")



    
