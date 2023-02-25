import sys
from pprint import pprint

t,w = map(int,sys.stdin.readline().split())

inputL = []

dp = [[[[-1] for _ in range(2+1)] for _ in range(t+1)] for _ in range(w+1)]

pprint(dp)

dp[1][0][w] = 0
dp[2][0][] = 0

for _ in range(t):
    whTree = int(sys.stdin.readline())
    dp[whTree][][w]

