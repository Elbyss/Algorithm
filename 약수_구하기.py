import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

a,b = map(int, input().split())
ans = []
for i in range(1, a+1):
  if (a % i == 0):
    ans.append(i)

if (len(ans) < b):
  print (0)
else:
  print (sorted(ans)[b-1])