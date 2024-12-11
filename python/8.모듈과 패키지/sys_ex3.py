#이전 문제 sys.exit(0)으로 고쳐보기
import sys

args = sys.argv
if (len(args)!=4):
    print("오류")
    sys.exit(0)

cmd = args[1]
num1 = int(args[2])
num2 = int(args[3])

if cmd == "mul" :
    print(num1*num2)
elif cmd == "add":
    print(num1 + num2)