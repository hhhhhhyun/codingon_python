#실습4.
import sys
stack = []
n = int(sys.stdin.readline()) #int(input()) 해도 되는데 속도가 더 빨라서 저렇게 쓰는거임 

def push(p) :
    stack.append(p)

def pop() :
    if stack :
        print(stack.pop())
    else :
        print(-1)

def size() :
    print(len(stack))

def empty() :
    print(1 if not stack else 0)

def top() :
    if stack :
        print(stack[-1])
    else :
        print(-1)

def stack_program() :
    input = sys.stdin.readline
    n = int(input().strip())

    for _ in range(n) :
         command = input().strip().split()
         if command[0] == "push" :
            push(int(command{1}))
         elif command[0] == "pop" :
            pop()
         elif command[0] == "size" :
            size()
         elif command[0] == "empty" :
            size()
         elif command[0] == "top" :
            top()

stack_program()
