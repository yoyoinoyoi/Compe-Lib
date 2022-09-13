s = input()
t = input()
S,T = len(s),len(t)
dp = [[0]*(T+1) for _ in range(S+1)]
ans = []
for i in range(1,S+1):
  for j in range(1,T+1):
    if s[i-1] == t[j-1]:
      dp[i][j] += dp[i-1][j-1] +1
    else:
      dp[i][j] = max(dp[i][j-1],dp[i-1][j])
      
#復元
while S*T:
  if dp[S][T] == dp[S-1][T]:
    S -= 1
  elif dp[S][T] == dp[S][T-1]:
    T -= 1
  else:
    ans.append(s[S-1])
    S -= 1
    T -= 1

#print(ans)
STR = ''
for i in ans[::-1]:
  STR += i
  
print(STR)
#print(dp)

"""
sample:
axyb
abyxb
"""