import time
import sys
sys.settrace

# Increase the recursion limit
sys.setrecursionlimit(1 * 10 ** 9)

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

algo_set = {
    'label': 'Fibonacci',
    'types': {
        'r': {'label': 'Recursive', 'function': fibonacci.recursive},
        'm': {'label': 'Memoized Top Down', 'function': fibonacci.memoizedTopDown},
        'b': {'label': 'Bottom Up', 'function': fibonacci.bottomUp},
    }
}

test_set, results, test_cases = ['r', 'm', 'b'], [], {'r': 5, 'm': 1*10**6, 'b': 5}

print('{:>2}.  {:^23}  {:^17}  {:<45} {:>14}'.format("No", "Algorithm", "Type", "Input", "Elapsed time"))
for algo_type in test_set:
    input = test_cases[algo_type]
    start_time = time.time()
    algo_set['types'][algo_type]['function'](input)
    duration = time.time() - start_time
    input_str = f'{input:,}'+' th fibonacci'
    line_new = '{:>2}.  {:^23}  {:^17}  {:<45} {:>14}'.format(len(results)+1, algo_set['label'], algo_set['types'][algo_type]['label'], input_str, f'{duration*1000:,.3f} ms')
    print(line_new)
    results.append([algo_set['label'], algo_set['types'][algo_type]['label'], input_str, duration * 1000])