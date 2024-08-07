import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input()) # 자릿수

dp = [[0]*10 for _ in range(n+1)]
dp[1][0] = 0 # 0으로 시작하는 수는 계단수가 아니므로 제외

for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  for j in range(10):
    if j == 0: # 뒤에 오는 자리가 0일 경우, 앞에는 무조건 1
      dp[i][j] = dp[i-1][1]
    elif j == 9: # 뒤에 오는 자리가 9일 경우, 앞에는 무조건 8
      dp[i][j] = dp[i-1][8] 
    else: # 그 외의 경우 (1~8)
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
  
print (sum(dp[n]) % 1000000000)