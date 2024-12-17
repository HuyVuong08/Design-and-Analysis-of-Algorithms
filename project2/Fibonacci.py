class Fibonacci:
    def recursive(self, n: int) -> int:
        if n <= 1:
            return n
        return self.recursive(n-1) + self.recursive(n-2)

    def memoizedTopDown(self, n: int, M = {}) -> int:
        if n in M:
            return M[n]
        if n <= 1:
            M[n] = n
            return n
        M[n] = self.memoizedTopDown(n-1, M) + self.memoizedTopDown(n-2, M)
        return M[n]

    def bottomUp(self, n: int) -> int:
        if n <= 1:
            return n
        M = [0] * (n+1)
        M[1] = 1
        for i in range(2, n+1):
            M[i] = M[i-1] + M[i-2]
        return M[n]

fibonacci = Fibonacci()
