import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
def tiling(n):
  dp = [0] * (n + 1)
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n + 1):  # 3 ~ 10 까지
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

  return dp[n]

n = int(input())
result = tiling(n)
print(result)