def main(A):#初期化
    Few = [0]*n
    for i in range(n):
      Few[i] += A[i]
    return Few

def fadd(i, x):#(i=1,2,...,n)
    while i <= n:
        Few[i-1] += x
        i += i & -i

def fsum(l, r):#a_L+...+a_r
    return Sum(r) - Sum(l-1)

def Sum(r):#a_1+...+a_r
    ans = 0
    while r > 0:
        ans += Few[r-1]
        r -= r & -r
    return ans

n = int(input())
A = list(map(int,input().split()))
Few = main(A)#初期化完了

print(Few)