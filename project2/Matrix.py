class OptimalMatrixChainMultiplication:
    def recursiveHelper(self, p: list[int], i=1, j=None, s=None) -> Union[int, list[list[int]]]:
        j = len(p) - 1 if j is None else j
        s = [[None] * len(p) for _ in range(len(p))] if s is None else s
        if i == j:
            return 0, s
        m = float('inf')
        for k in range(i, j):
            l, s = self.recursiveHelper(p, i, k, s)
            r, s = self.recursiveHelper(p, k + 1, j, s)
            q = l + r + p[i - 1] * p[k] * p[j]
            if q < m:
                m = q
                s[i][j] = k
        return m, s

    def recursive(self, p: list[int]) -> Union[int, str]:
        m, s = self.recursiveHelper(p)
        output = self.printOptimalParenthesis(s) + f" with cost {m:,}"
        return output

    def memoizedTopDownHelper(self, p: list[int], i=1, j=None, s=None, M=None) -> Union[int, list[list[int]]]:
        j = len(p) - 1 if j is None else j
        s = [[None] * len(p) for _ in range(len(p))] if s is None else s
        M = [[float('inf')] * len(p) for _ in range(len(p))] if M is None else M
        if M[i][j] != float('inf'):
            return M[i][j], s
        if i == j:
            return 0, s
        for k in range(i, j):
            l, s = self.memoizedTopDownHelper(p, i, k, s, M)
            r, s = self.memoizedTopDownHelper(p, k + 1, j, s, M)
            q = l + r + p[i - 1] * p[k] * p[j]
            if q < M[i][j]:
                M[i][j] = q
                s[i][j] = k
        return M[i][j], s

    def memoizedTopDown(self, p: list[int]) -> Union[int, str]:
        m, s = self.memoizedTopDownHelper(p)
        output = self.printOptimalParenthesis(s) + f" with cost {m:,}"
        return output

    def bottomUpHelper(self, p: list[int]) -> Union[int, list[list[int]]]:
        M = [[0 for _ in range(len(p))] for _ in range(len(p))]
        s = [[0 for _ in range(len(p))] for _ in range(len(p))]
        for l in range(2, len(p)):
            for i in range(1, len(p) - l + 1):
                j = i + l - 1
                M[i][j] = float('inf')
                for k in range(i, j):
                    q = M[i][k] + M[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if q < M[i][j]:
                        M[i][j] = q
                        s[i][j] = k
        return M[1][len(p) - 1], s

    def bottomUp(self, p: list[int]) -> Union[int, str]:
        m, s = self.bottomUpHelper(p)
        output = self.printOptimalParenthesis(s) + f" with cost {m:,}"
        return output

    def printOptimalParenthesis(self, s: list[list[int]], i=1, j=None) -> str:
        j = len(s)-1 if j is None else j
        parenthisis = ""
        if i == j:
            parenthisis += f"A{i}"
        else:
            parenthisis += "("
            parenthisis += self.printOptimalParenthesis(s, i, s[i][j])
            parenthisis += self.printOptimalParenthesis(s, s[i][j] + 1, j)
            parenthisis += ")"
        return parenthisis

matrixChain = OptimalMatrixChainMultiplication()