import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = [0] + [int(input()) for _ in range(1, n+1)]
dp = [0] * (n+1)
dp[1] = arr[1]

if n > 1:
    dp[2] = arr[1] + arr[2]
    
for i in range(3, n+1):
  dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    
print (dp[n])