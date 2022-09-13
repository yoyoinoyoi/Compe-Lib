# n以下の素数をリスト型で返す
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
            
    p_list = [i for i in range(n + 1) if is_prime[i]]
    return p_list

# ----------------------------

N = int(input())
print(len(primes(N)))