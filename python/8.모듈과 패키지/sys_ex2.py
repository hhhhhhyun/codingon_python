#3개를 입력 받는데 mul이면 두 수를 곱하고 add면 두 수를 더해라
#ex) a.py mul 2 3
#    6
#    a. py add 4 5
#    9
#    (입력이 2개 이하거나 4개 이상이면 오류처리)
import sys

args = sys.argv
if (len(args)!=4):
    print("오류") # = sys.exit(0)

else:
    cmd = args[1]
    num1 = int(args[2])
    num2 = int(args[3])

    if cmd == "mul" :
        print(num1*num2)
    elif cmd == "add":
        print(num1 + num2)
    