import sys
x= sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
# dp 테이블 초기화
dp =[[0]*(len(y)+1) for _ in range(len(x)+1)]

for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        # 문자열이 같을 때 1을 더함
        if x[i-1]==y[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        # 문자열이 같지 않을 때 두 값 중 큰 값
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# dp 테이블에서 출력
print(dp[-1][-1])






