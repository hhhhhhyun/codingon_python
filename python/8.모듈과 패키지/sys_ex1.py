#sys모듈
import sys

print(sys.argv)

args = sys.argv[1:]
print(args)
print()

#실습0. 사용자가 입려간 모든 숫자를 더하는 프로그램을 만들어라
#(argv사용)
args = sys.argv[1:]
print(args)

total = 0
for i in args:
    total += int(i)

print("합계 :", total)