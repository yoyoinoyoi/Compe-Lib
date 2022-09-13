import sys
sys.setrecursionlimit(10**7)
r,c = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
Map = [list(input()) for _ in range(r)]

def dfs(x,y,t):
  if not(0<=x<c) or not(0<=y<r) or Map[x][y] == '#':
    return
  
  if type(Map[x][y]) is str:
    Map[x][y] = t
    
  dfs(x+1,y,t)
  dfs(x,y+1,t)
  dfs(x-1,y,t)
  dfs(x,y-1,t)

dfs(sx-1,sy-1,0)
print(Map)
print(Map[gx-1][gy-1])