# Project 2: Dynamic Programming

## Bonus

### Recursive Fibonacci

A practical input is 51 where the users would need to wait about 1,3 hours to get the result as shown in the screenshot below. The recursive approach is not efficient for large inputs.

![Extra1](extra1.png)

### Memoized Top Down Fibonacci

The memoized top down approach is more efficient than the recursive approach. It only takes about 0.000001 seconds to get the result for the input of 51.

A practical input is around $10^5$ where larger inputs would exceed the maximum recursion depth. The memoized top down approach is not efficient for extremely large inputs.

In practice, the bottom up approach takes around 0.006 ms to get the result for the input of 10^5 as illustrated in the screenshot below.

![Extra2](extra2.png)

### Bottom Up Fibonacci

The bottom up approach is the most efficient approach. It only takes about 0.000001 seconds to get the result for the input of 51.

A practical input is around $10^6$ where larger inputs would exceed the maximum (24 bytes) of memory for the `Python` programming language. For instance, a Fibonacci 10^6th would be around 2.1 \* 10^5 digits long.

In practice, the bottom up approach takes around 240 ms to get the result for the input of 10^6 as illustrated in the screenshot below.

![Extra3](extra3.png)

## Introduction

### Fibonacci

#### Problem Statement

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with `0` and `1`. The sequence goes: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, `and so on.

#### Problem Solution

The Fibonacci sequence can be solved using dynamic programming. There are three common ways to solve the Fibonacci sequence using dynamic programming: recursive, memoized top down, and bottom up.

##### Recursive

The recursive solution is the most intuitive. It is also the most inefficient. The time complexity is $O(2^n)$ because each call to `fib(n)` makes two recursive calls to `fib(n-1)` and `fib(n-2)`.

##### Memoized Top Down

The memoized top down solution is more efficient than the recursive solution. It uses a cache to store the results of previous calculations. This way, if the same value is calculated twice, it can be retrieved from the cache instead of being calculated again. The time complexity is $O(n)$ because each value is calculated once.

##### Bottom Up

The bottom up solution is the most efficient. It uses a table to store the results of previous calculations. This way, each value is calculated once and only once. The time complexity is O(n) because each value is calculated once.

### Matrix Chain Multiplication

#### Problem Statement

Matrix chain multiplication is an optimization problem that involves finding the most efficient way to multiply a chain of matrices. The problem is to find the minimum number of multiplications needed to multiply a chain of matrices.

#### Problem Solution

The matrix chain multiplication problem can be solved using dynamic programming. The solution involves creating a table to store the results of previous calculations. The table is filled in using a bottom up approach. The time complexity is $O(n^3)$ because there are $n^2$ subproblems and each subproblem takes $O(n)$ time to solve. Another approach is to use a memoized top down approach. The time complexity is $O(n^3)$ because there are $n^2$ subproblems and each subproblem takes $O(n)$ time to solve.

ALso a recursive approach can be used. The time complexity is O(2^n) because each call to `mcm(i, j)` makes two recursive calls to `mcm(i, k)` and `mcm(k, j)`.

## why is dynamic programming interesting/useful

Dynamic programming is interesting because it is a method for solving complex problems by breaking them down into simpler subproblems. It is useful for solving optimization problems that can be broken down into subproblems. Additionally, It is useful for solving problems that have overlapping subproblems.

Dynamic programming stores previously computed data in a table to avoid redundant calculations if the same subproblem is encountered again. This makes it more efficient than other approaches. Dynamic programming is useful for solving optimization problems that can be broken down into subproblems. Additionally, It is useful for solving problems that have overlapping subproblems.

## Runs showing output

![List of runs](list.png)

## Results

| Problem                 | Algorithm         | Input          |  Runtime (ms) |
| :---------------------- | :---------------- | :------------- | ------------: |
| Fibonacci               | Recursive         | 30th fibonacci |       191.066 |
| Fibonacci               | Memoized Top Down | 30th fibonacci |         0.011 |
| Fibonacci               | Bottom Up         | 30th fibonacci |         0.005 |
| Fibonacci               | Recursive         | 35th fibonacci |       2197.96 |
| Fibonacci               | Memoized Top Down | 35th fibonacci |         0.003 |
| Fibonacci               | Bottom Up         | 35th fibonacci |         0.006 |
| Fibonacci               | Recursive         | 40th fibonacci |       23515.5 |
| Fibonacci               | Memoized Top Down | 40th fibonacci |         0.005 |
| Fibonacci               | Bottom Up         | 40th fibonacci |         0.007 |
| Fibonacci               | Recursive         | 45th fibonacci |        262305 |
| Fibonacci               | Memoized Top Down | 45th fibonacci |         0.021 |
| Fibonacci               | Bottom Up         | 45th fibonacci |         0.007 |
| Fibonacci               | Recursive         | 51th fibonacci | 4,698,324.234 |
| Fibonacci               | Memoized Top Down | 51th fibonacci |         0.038 |
| Fibonacci               | Bottom Up         | 51th fibonacci |         0.013 |
| Opt. Matrix Chain Multi | Recursive         | 10 matricies   |         5.415 |
| Opt. Matrix Chain Multi | Memoized Top Down | 10 matricies   |         0.144 |
| Opt. Matrix Chain Multi | Bottom Up         | 10 matricies   |         0.071 |
| Opt. Matrix Chain Multi | Recursive         | 15 matricies   |       1251.43 |
| Opt. Matrix Chain Multi | Memoized Top Down | 15 matricies   |         0.407 |
| Opt. Matrix Chain Multi | Bottom Up         | 15 matricies   |         0.154 |
| Opt. Matrix Chain Multi | Recursive         | 17 matricies   |       11048.1 |
| Opt. Matrix Chain Multi | Memoized Top Down | 17 matricies   |         0.531 |
| Opt. Matrix Chain Multi | Bottom Up         | 17 matricies   |         0.207 |
| Opt. Matrix Chain Multi | Recursive         | 20 matricies   |    308368.208 |
| Opt. Matrix Chain Multi | Memoized Top Down | 20 matricies   |         0.854 |
| Opt. Matrix Chain Multi | Bottom Up         | 20 matricies   |         0.326 |
| Opt. Matrix Chain Multi | Recursive         | 22 matricies   | 2,726,292.455 |
| Opt. Matrix Chain Multi | Memoized Top Down | 22 matricies   |         1.277 |
| Opt. Matrix Chain Multi | Bottom Up         | 22 matricies   |         0.453 |

## Run time analysis

![Table of Actual Performance](table.png)

### Expectations and Results

#### Fibonacci

The recursive approach has a time complexity of O(2^n) which shows exponential growth when n increases. The memoized top down and bottom up approaches have a time complexity of O(n) which shows linear growth. The recursive approach is expected to have the worst performance, followed by the memoized top down approach, and the bottom up approach.

#### Matrix Chain Multiplication

The recursive approach has a time complexity of O(2^n) which shows exponential growth when n increases. The memoized top down and bottom up approaches have a time complexity of O(n^3) which shows cubic growth. The recursive approach is expected to have the worst performance, followed by the memoized top down approach, and the bottom up approach.

## Anomalies

The run time of `fib(35)` is faster than the that of `fib(30)` for the memoized top down approach. This is likely due to task rotation and other processes running on the computer at the time of the run.
