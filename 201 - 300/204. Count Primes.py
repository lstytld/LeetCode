class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1] * n
        isPrime[0:2] = [0,0]
        i = 0
        while i**2 < n:
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = 0
            i += 1
        return sum(isPrime)