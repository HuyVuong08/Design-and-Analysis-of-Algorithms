# Homework 4:

## Problem 1:

### **a.** Recursive implementation based on the definition to compute the nth Fibonacci number

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### **b.** Recursion tree for F6.

```javascript
                     F6
              /            \
            F5              F4
        /        \         /  \
      F4          F3     F3    F2
     /   \       / \    / \   / \
    F3    F2    F2 F1  F2 F1 F1 F0
   / \   / \   / \    / \
  F2 F1 F1 F0 F1 F0  F1 F0
 / \
F1 F0
```

<div style="page-break-after: always;"></div>

### **c.** Memoized version of the algorithm

```python
M = {}
def fib(n: int) -> int:
    if n in M:
        return M[n]
    if n <= 1:
        M[n] = n
        return n
    M[n] = fib(n-1) + fib(n-2)
    return M[n]
```

### **d.** Recursion tree for F6

```javascript
           F6
          /  \
        F5   M[4]
       /  \
      F4  M[3]
     /  \
    F3  M[2]
   / \
  F2 M[1]
 / \
F1 F0
```

### **e.** Bottom-up version of the algorithm

```javascript
def fib(self, n: int) -> int:
    if n <= 1:
        return n
    M = [0] * (n+1)
    M[1] = 1
    for i in range(2, n+1):
        M[i] = M[i-1] + M[i-2]
    return M[n]
```

<div style="page-break-after: always;"></div>

## Problem 2:

Bottom-up dynamic programming algorithm

```javascript
def MODIFIED-CUT-ROD(p: list[int], l: int, c: int) -> int:
    dp = [0] * (l + 1)
    for i in range(1, l + 1):
        res = float('-inf')
        for j in range(1, i + 1):
            cost = 0 if j == i else c
            res = max(res, dp[i - j] + p[j - 1] - cost)
            dp[i] = res
    return dp[l]
```

<div style="page-break-after: always;"></div>

## Problem 3:

Modify MEMOIZED-CUT-ROD to return not only the value but the actual solution, too

```javascript
def MEMOIZED-CUT-ROD-MODIFIED(p: list[int], l: int, memo = {}, sol = {}):
    if l in memo:
        return memo[l], sol
    if l == 0:
        memo[l] = 0
        return 0, sol
    q = float("-inf")
    for i in range(1, l + 1):
        revenue, solution = MEMOIZED-CUT-ROD-MODIFIED(p, l - i, memo, sol)
        revenue += p[i - 1]
        if q < revenue:
            q = revenue
            sol[l] = i
    memo[l] = q
    return memo[l], sol
```

<div style="page-break-after: always;"></div>

## Problem 4:

```javascript
   i 0  1   2  3  4   5
p = [2, 3, 10, 5, 4, 20];

```

### The Table

| i \ j | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 60=2x3x10<br />size=2x10 <br />s=1 <br />seq=1 | 160=<br />min(60+2x10x5,<br />150+2x3x5)<br />size=2x5 <br />s=2<br />seq=5 | 200=<br />min(160+2x5x4,<br />210+2x3x4,<br />60+200+2x10x4)<br />size=2x4<br />s=3<br />seq=8 | 360=<br />min(200+2x4x20,<br />450+2x3x20,<br />160+400+2x5x20,<br />60+1000+2x10x20)<br />size=2x20<br />s=4<br />seq=10 |
| 2 | 0 | 0 | 150=3x10x5<br />size=3x5<br />s=2<br />seq=2 | 210=<br />min(150+3x5x4,<br />200+3x10x4)<br />size=3x4<br />s=3<br />seq=6 | 450=<br />min(210+3x4x20,<br />1000+3x10x20,<br />150+400+3x520)<br />size=3x20<br />s=4<br />seq=9 |
| 3 | 0 | 0 | 0 | 200=10x5x4<br />size=10x4<br />s=3<br />seq=3 | 1000=<br />min(200+10x4x20,<br />400+10x5x20)<br />size=10x20<br />s=4<br />seq=7 |
| 4 | 0 | 0 | 0 | 0 | 400=5x4x20<br />size=5x20<br />s=4<br />seq=4 |
| 5 | 0 | 0 | 0 | 0 | 0 |

The optimal parenthesis is:

`((((A1.A2).A3).A4).A5)`
