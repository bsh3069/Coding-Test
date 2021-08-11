# 회사에 있는사람
# 자유로운 출퇴근 시간, 로그가 주어졌을 때 회사에 있는 모든 사람을 구하는 프로그램 작성
# 출입 기록의 수 n
import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for _ in range(n):
    name,record = map(str,input().split())
    if record =='enter':
        dict[name] = 1
    else:
        del dict[name]
# key값을 기준으로 정렬
dict = sorted(dict, reverse= True)
# 람다를 이용해 value값 기준으로 정렬
# sorted(dict, key = lambda x:dict[x])
for i in dict:
    print(i)
