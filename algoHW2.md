# Homework 2

## Problem 1:

b. 
$$
\begin{aligned}
    & \text{We have } T(n) = 2T(n/4) + \sqrt n\\
    & \implies f(n) = \sqrt n = n^{1/2}\\
    & \text{We have } ws(n) = n^{\lg_{4} 2} = n^{1/2}\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{ws(n)} = \frac{n^{1/2}}{n^{1/2}} = 1\\
    & \implies f(n) = \Theta(ws(n)\lg^k n) \text{ with } k=0\\
    & \implies T(n) = \Theta(n^{1/2}\lg n)
\end{aligned}
$$

c. 
$$
\begin{aligned}
    & \text{We have } T(n) = 2T(n/4) + \sqrt n.lg^2n\\
    & \implies f(n) = \sqrt n . \lg^2 n = n^{1/2} . \lg^2 n\\
    & \text{We have } ws(n) = n^{\lg_{4} 2} = n^{1/2}\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{\frac{ws(n)}{\ln \epsilon}} = \frac{n^{1/2} . \lg^2 n}{\frac{n^{1/2}}{\lg \epsilon}} = \lg^2 n \cdot \lg \epsilon = \infty\\
    & \implies f(n) = \Omega(\frac{ws(n)}{\lg \epsilon}) \text{ with } \epsilon > 0\\
    & \implies T(n) = \Theta(f(n)) = \Theta(\sqrt n \lg^2 n)
\end{aligned}
$$

d. 
$$
\begin{aligned}
    & \text{We have } T(n) = 2T(n/4) + n\\
    & \implies f(n) = n\\
    & \text{We have } ws(n) = n^{\lg_{4} 2} = n^{1/2}\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{\frac{ws(n)}{\ln \epsilon}} = \frac{n}{\frac{n^{1/2}}{\lg \epsilon}} = n^{1/2} \cdot \lg \epsilon = \infty\\
    & \implies f(n) = \Omega(\frac{ws(n)}{\lg \epsilon}) \text{ with } \epsilon > 0\\
    & \implies T(n) = \Theta(f(n)) = \Theta(n)
\end{aligned}
$$

\pagebreak

## Problem 2:

We analyze the time complexity step by step:

- Outer loop:

The outer loop starts with `i = n` and continues while `i >= 1`, with `i` being halved at each step (`i = ⌊i/2⌋`).

This halving means that the number of iterations of the outer loop is $\lg 𝑛$ ​ because the value of i decreases as $n, n/2, n/4, \cdots, 1$.
⁡
- Inner loop:

For each value of `i`, the inner loop starts with `j = i` and continues while `j <= n`, doubling `j` at each step (`j = 2 * j`).

The inner loop increases `j` as $i, 2i, 4i, \cdots, n$ so the number of iterations for the inner loop is proportional to $\lg (n / i)$.

$$
\begin{aligned}
    T(n) = & \sum^{\lg n}_{i = 1} \sum^{\lg (n/i)}_{j=i}1\\
    = & \sum^{\lg n}_{i = 1} \Theta(\lg (n / i))\\
    = & \Theta(\sum^{\lg n}_{i = 1} \lg (n)) - \Theta(\sum^{\lg n}_{i = 1} \lg (i))\\
    = & \Theta(\lg^2 n)
\end{aligned}
$$

Therefore, we have $T(n) = \Theta(\lg^2 n)$

\pagebreak

## Problem 3:

Given the array

```javascript
   i  1   2   3   4   5   6   7    8    9
A = [12, 34, 37, 45, 57, 82, 95, 100, 134]

target = 100
```

- <ins>Step 1</ins>:

Find the mid point $\frac{1 + 9}{2} = 5$

- <ins>Step 2</ins>:

Since `A[5] != 100` and `A[5] < 100`, we recursively search in the subaray `A[6 : 9]`.

- Repeat <ins>Step 1</ins>:

Find the mid point $\lfloor\frac{6 + 9}{2}\rfloor = 7$

- Repeat <ins>Step 2</ins>:

Since `A[7] != 100` and `A[7] < 100`, we recursively search in the subaray `A[8 : 9]`.

- Repeat <ins>Step 1</ins>:

Find the mid point $\lfloor\frac{8 + 9}{2}\rfloor = 8$

- Repeat <ins>Step 2</ins>:

Since `A[8] == 100`, we terminate and return 8.

\pagebreak

## Problem 4:

a. 

Given the list as illustrated below:

```javascript
   i   1   2    3   4    5   6  7    9 
A = [123, 34, 189, 56, 150, 12, 9, 240]
```

- <ins>Step 1</ins>:
Calculate mid piont by the following function:

$$
\begin{aligned}
    mid = &\frac{right - left}{2}\\
    = &\frac{9 - 1}{2}\\
    = &4
\end{aligned}
$$

- <ins>Step 2</ins>:

Devide the array `A` into 2 subarrays 

- Array `B` is `[left, mid]`

```javascript
   i   1   2    3   4
B = [123, 34, 189, 56]
```

- Array `C` is `[mid, right]`

```javascript
   i   5   6  7    9 
C = [150, 12, 9, 240]
```

- <ins>Step 3</ins>:

Repeat <ins>Step 1</ins> and <ins>Step 2</ins> for subarray `B` and `C`

The array `B` will be halved into array `D` and `E` as illustrated below:

```javascript
   i   1   2    3   4
B = [123, 34, 189, 56]
```

mid = 

```javascript
D = []
```

Repeat until array size is 1

- <ins>Step 4</ins>:

Merge subarrays into the orignal array `A`

We merge these pairs of subarrays together:
- `[123]` and `[34]` becomes `[34, 123]`
- `[189]` and `[56]` becomes `[56, 189]`
- `[150]` and `[12]` becomes `[12, 150]`
- `[9]` and `[240]` becomes `[9, 240]`

Then we continue to merge these pairs of subarrays together:
- `[34, 123]` and `[56, 189]` becomes `[34, 56, 123, 189]`
- `[12, 150]` and `[9, 240]` becomes `[9, 12, 150, 240]`

Then we continue to merge this pairs of subarrays together:
- `[34, 56, 123, 189]` and `[9, 12, 150, 240]` becomes `[9, 12, 34, 56, 123, 150, 189 240]`

b. 

The tree for dividing

```javascript
       [123,34,189,56,150,12,9,240]
        /                         \
  [123,34,189,56]          [150,12,9,240]
   /            \          /            \
 [123,34]    [189,56]    [150,12]   [9,240]
  /     \    /     \      /    \    /     \
[123] [34] [189]  [56] [150]  [12] [9]   [240]
```

The tree for merging

```javascript
[123] [34] [189]  [56] [150]  [12] [9]   [240]
  \     /    \     /      \    /    \     /
 [34,123]    [56,189]    [12,150]   [9,240]
   \            /          \            /
  [34,56,123,189]          [9,12,150,240]
        \                        /
       [9,12,34,56,123,150,189,240]
```

\pagebreak

## Problem 5:

a. 

$$
\begin{aligned}
    & \text{We have recurrence of binary search is:}\\
    & T(n) = T(n/2) + \Theta(1)\\
    & \implies f(n) = 1\\
    & \text{We have } ws(n) = n^{\lg_{2} 1} = n^{0} = 1\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{ws(n)} = 1\\
    & \implies f(n) = \Theta(ws(n)) \text{ with } k = 0\\
    & \implies T(n) = \Theta(ws(n) \cdot \lg n) = \Theta(\lg n)
\end{aligned}
$$

Binary search needs a maximum of 2 comparisons per iteration and the maximum iteration for input size of 100,000 is $\lg 100000$. Therefore, the maximum number of comparisons operations before finding a given item or concluding that it is not in the list is $2\lg 100000$

b. 

$$
\begin{aligned}
    & \text{We have recurrence of ternary search is:}\\
    & T(n) = T(n/3) + \Theta(1)\\
    & \implies f(n) = 1\\
    & \text{We have } ws(n) = n^{\lg_{3} 1} = n^{0} = 1\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{ws(n)} = 1\\
    & \implies f(n) = \Theta(ws(n)) \text{ with } k = 0\\
    & \implies T(n) = \Theta(ws(n) \cdot \lg n) = \Theta(\lg n)
\end{aligned}
$$

Therefore, there no significant improvement when using ternary search over binary search as both of which have time complexity $T(n) = \Theta(\lg n)$. 

As a side note, although ternary search needs fewer steps (lower height in the recursion tree), ternary search requires more comparision operations (max 4 comparisions per iteration) than binary search (max 2 comparisions per iteration). Therefore, ternary search is inferior to binary search.

\pagebreak

## Problem 6:

Pseudocode for ternary search

Base case: if `A.length <= 0`, return `key` not found

<ins>Step 1</ins>: Find the `one_third` and `two_thirds` point of the array `A`

<ins>Step 2</ins>: Assess if `A[one_third] == key`

* If `True`, return `one_third` which is the index of the `key` in the array `A`
* Else if `False`, assess if `A[two_thirds] == key` 
* Else if `True`, return `two_thirds` which is the index of the `key` in the array `A`
* Else if `False`, move to `Step 3`

<ins>Step 3</ins>: Recursively search the array

* if `A[one_third] > key` recursive call on the left partition
    * `Ternary_Search(A[1 : one_third - 1])`
* if `A[two_thirds] > key` and `A[one_third] < key` recursive call on the middle partition
    * `Ternary_Search(A[one_third + 1 : two_thirds - 1])`
* if `A[two_thirds] < key` recursive call on the right partition
    * `Ternary_Search(A[two_thirds + 1 : A.length])`

```javascript
function Recursive(A, key, low, high) {
    // Base case:
    if low > high
        return -1 // key not found

    // Step 1: calculate the mid point
    one_third = math.floor((low + high) / 3)
    two_thirds = math.floor(2 * (low + high) / 3)

    if A[one_third] == key // Step 2: assess A[mid] == key
        return one_third
    else if A[two_thirds] == key
        return two_thirds
    else if A[one_third] > key // Step 3: recursive call on left partition
        return Recursive(A, key, low, one_third - 1)
    else if A[two_third] < key // Step 3: recursive call on right partition
        return Recursive(A, key, two_thirds + 1, high)
    else // Step 3: recursive call on middle partition
        return Recursive(A, key, one_third + 1, two_thirds - 1)
}
    
function TernarySearch(A : array, key) { // A's indices start from 1
    return Recursive(A, key, 1, A.length)
}
```

Time complexity $T(n)$ analysis using master theorem.

$$
\begin{aligned}
    & \text{We have recurrence of ternary search is:}\\
    & T(n) = T(n/3) + \Theta(1)\\
    & \implies f(n) = 1\\
    & \text{We have } ws(n) = n^{\lg_{3} 1} = n^{0} = 1\\
    & \text{We have } \lim_{x \to \infty} \frac{f(n)}{ws(n)} = 1\\
    & \implies f(n) = \Theta(ws(n)) \text{ with } k = 0\\
    & \implies T(n) = \Theta(ws(n) \cdot \lg n) = \Theta(\lg n)
\end{aligned}
$$

Base on the code, after one iteration, the input size is reduced by a third. Therefore, we have the time complexity $T(n) = \lg_3 n$. In each iteration, there were at most 4 comparision operation. Hence, we have the time complexity is $T(n) = 4c\lg_3 n$ where c is constant.