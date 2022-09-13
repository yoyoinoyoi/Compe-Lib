import sys
from collections import deque

#辺を受け取る(無向)
 
N,Q = map(int,input().split())
path = [[] for _ in range(N)]
for _ in range(N-1):
  a,b = map(int,input().split())
  path[a-1].append(b)
  path[b-1].append(a)

#ノードに値がある場合

cnt = [0]*N
for _ in range(Q):
  t,val = map(int,input().split())
  cnt[t-1] += val
  
depth = [-1]*N
depth[0] = 0
ans = [0]*N
ans[0] = cnt[0]

#木の深さを取得
#popleft() を pop()に変えてやると深さ優先
q = deque([1])
while q:
  next = q.popleft()
  for i in path[next-1]:
    if depth[i-1] == -1:
      q.append(i)
      depth[i-1] = (depth[next-1] + 1)
      #ans[i-1] += (ans[next-1] + cnt[i-1])
      
print(*ans)