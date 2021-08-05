# input으로 받으면 시간초과 발생
기존 사용한 방법 
while True:
    try:
        print(input())
    except EOFError:
        break
        
시간 초과 방지한 방법
import sys
a = sys.stdin.read()
print(a)
