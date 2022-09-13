class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def fadd(self, i, x):#(i=1,2,...,n)
        if 0 < i <= self._n:
            while i <= self._n:
                self.data[i - 1] += x
                i += i & -i

    def fsum(self, l, r):#a_L+...+a_r
        if 0 < l <= r <= self._n:
            return self.Sum(r) - self.Sum(l-1)

    def Sum(self, r):#a_1+...+a_r
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
