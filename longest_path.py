import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
path_for = [[] for _ in range(N)]
ans = 0
for i in range(M):
  x,y = map(int,input().split())
  path_for[x-1].append(y-1)

dp = [-1]*N
def dfs(v):
    if dp[v] == -1:
      dp[v] = max(dfs(w) for w in path_for[v]) + 1 if path_for[v] else 0
    return dp[v]

for v in range(N):
  a = dfs(v)
  ans = max(ans,a)
  #print(a)
print(ans)