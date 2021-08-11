s = list(input())
t = list(input())
# s를 t로 만드는문제 -> t를 s로 만들자!
# 문자열의 길이가 같아질때 까지 반복
while len(s)!=len(t):
    if t[-1]=='A':
        # pop함수는 리스트 맨 마지막 요소를 돌려주고 삭제
        # 기존 문제는 A를 추가하므로 pop을 이용해서삭제
        t.pop()
    elif t[-1]=='B':
        # 기존 문제는 B를 추가하므로 삭제
        t.pop()
        t =t[::-1]
    if s==t:
        break
if s==t:
    print(1)
else:
    print(0)
