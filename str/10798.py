# 5개의 입력
s = [input() for i in range(5)]
# 문자열 마다 최대 길이가 다름
max_len = 0
if len(s) > max_len:
    max_len = len(s)
# 이중  for문 사용
for i in range(max_len):
    for j in range(len(s)):
        if i>=len(s[j]):
            continue
        else:
            print(s[j][i], end='')
