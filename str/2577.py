# 숫자 입력
a = int(input())
b = int(input())
c = int(input())
# 곱셈 결과를 문자열로 만들고 리스트에 넣음
total = list(str(a*b*c))
# 0-9까지 range(10) / for문을 통해 0-9까지 숫자를 반환
for i in range(10):
    print(total.count(str(i)))
