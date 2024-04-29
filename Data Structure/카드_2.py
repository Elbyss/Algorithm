import sys
from collections import deque as dq
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

queue = dq([i for i in range(1, n+1)])

while (len(queue) > 1):
  queue.popleft()
  queue.append(queue[0])
  queue.popleft()
print (*queue)