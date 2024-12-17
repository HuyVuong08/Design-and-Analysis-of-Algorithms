# Warm-Up Homework #0

## Problem 1

We have an example 2D array `A` being converted into 1D array `B` in row major as illustrated below.

```python
R = 3 // number of rows
C = 4 // number of columns

A = [
     j 1  2   3   4
    i
    1 [1, 2,  3,  4],
    2 [5, 6,  7,  8],
    3 [9, 10, 11, 12],
]

   k 1  2  3  4  5  6  7  8  9  10  11  12
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
```

From the 2D array A above, the value of k for elements in each rows will be in the ranges below:

-   For `i = 1` (first row)

$$
k \in [1 : C]
$$

-   For `i = 2` (second row)

$$
k \in [C+1 : 2 \times C]
$$

From the 2D array A above, for every elements in the first column (`j = 1`), the k will have values as below:

-   For `j = 1, i = 1` and `C` is in the number of columns

$$
\begin{aligned}
k &= j + (i - 1) \times C\\
&= 1 + 0 \times C\\
&= 1
\end{aligned}
$$

-   For `j = 1, i = 2` and `C` is in the number of columns

$$
\begin{aligned}
k &= j + (i - 1) \times C\\
&= 1 + 1 \times C\\
&= 5
\end{aligned}
$$

-   For `j = 1, i = 3` and `C` is in the number of columns

$$
\begin{aligned}
k &= j + (i - 1) \times C\\
&= 1 + 2 \times C\\
&= 9
\end{aligned}
$$

Therefore, we have the `k` index for each element in row `i` and column `j` is `(i - 1) * C + offset` where `C` is the number of columns. The `offset` is this case is the column index of the element (`j`).

In conclusion, we have the formular for `k` below:

$$
k = j + (i - 1) \times C
$$

Where `i` is the row index (starting with 1) and `j` is the column index (starting wiht 1) of the element, `C` is the number of columns in the 2D array `A`

\pagebreak

## Problem 2

We have an example 2D array `A` being converted into 1D array `B` in column major as illustrated below.

```python
R = 3 // number of rows
C = 4 // number of columns

A = [
     j 1  2   3   4
    i
    1 [1, 2,  3,  4],
    2 [5, 6,  7,  8],
    3 [9, 10, 11, 12],
]

   k 1  2  3  4  5  6   7  8  9   10 11 12
B = [1, 5, 9, 2, 6, 10, 3, 7, 11, 4, 9, 12],
```

From the 2D array A above, the value of k for elements in each column will be in the ranges below:

-   For `j = 1` (first column)

$$
k \in [1 : R]
$$

-   For `j = 2` (second column)

$$
k \in [R + 1 : 2 \times R]
$$

From the 2D array A above, for every elements in the first row (`i = 1`), the k will have values as below:

-   For `j = 1, i = 1` and `R` is in the number of columns\

$$
\begin{aligned}
k &= i + (j - 1) \times R\\
&= 1 + 0 \times R\\
&= 1
\end{aligned}
$$

-   For `j = 2, i = 1` and `R` is in the number of columns

$$
\begin{aligned}
k &= i + (j - 1) \times R\\
&= 1 + 1 \times R\\
&= 4
\end{aligned}
$$

-   For `j = 3, i = 1` and `R` is in the number of columns

$$
\begin{aligned}
k &= i + (j - 1) \times R\\
&= 1 + 2 \times R\\
&= 7
\end{aligned}
$$

Similar to `Problem 1`, we have the `k` index for each column `j` and row `i` is `(j - 1) * R + offset` where `R` is the number of rows. The `offset` is this case is the row index of the element (`i`).

Therefore, we have the formular for `k` below:

$$
k = i + (j - 1) \times R
$$

Where `i` is the row index (starting with 1) and `j` is the column index (starting wiht 1) of the element, `R` is the number of rows in the 2D array `A`

\pagebreak

## Problem 3

We have an example 2D array `A` being converted into 1D array `B` in column major as illustrated below.

```python
N = 5 // N is the number of cities

A = [
     j 1  2     3     4    5
    i
    1 [0, a12,  a13,  a14, a15],
    2 [x, 0,    a23,  a24, a25],
    3 [x, x,    0,    a34, a35],
    4 [x, x,    x,    0,   a45],
    5 [x, x,    x,    x,   0],
]

   k 1    2    3    4    5    6    7    8    9    10
B = [a12, a13, a14, a15, a23, a24, a25, a34, a35, a45]
```

From the 2D array A above, the distances from the first city are stored in the first row (`i = 1`). Similarly the distances from the second city are stored in the second row (`i = 2`).

The value of k for elements in each rows will be listed below:

-   For `i = 1` (first row)

The index `k` starts from

$$
\begin{aligned}
&(i - 1) \times N - \sum^{i-1}_{u=0}u + 1\\
= &(1 - 1) \times N - \sum^{1-1}_{u=0}u + 1\\
= & 0 - 0 + 1\\
= &1
\end{aligned}
$$

-   For `i = 2` (second row)

The index `k` starts from

$$
\begin{aligned}
&(i - 1) \times N - \sum^{i-1}_{u=0}u + 1\\
= &(2 - 1) \times N - \sum^{2-1}_{u=0}u + 1\\
= &N - 1 + 1\\
= &5
\end{aligned}
$$

-   For `i = 3` (third row)

The index `k` starts from

$$
\begin{aligned}
&(i - 1) \times N - \sum^{i-1}_{u=0}u + 1\\
= &(3 - 1) \times N - \sum^{3-1}_{u=0}u + 1\\
= &2 \times N - 3 + 1\\
= &8
\end{aligned}
$$

-   For `i = 4` (third row)

The index `k` starts from

$$
\begin{aligned}
&(i - 1) \times N - \sum^{i-1}_{u=1}u + 1\\
= &(4 - 1) \times N - \sum^{4-1}_{u=1}u + 1\\
= &3 \times N - 6 + 1\\
= &10
\end{aligned}
$$

The value of k for elements in column 4th will be listed below:

-   For `i = 1` and `j = 4`

$$
\begin{aligned}
k = &(i - 1) \times N - \sum^{i-1}_{u=0}u + 1 + (j - i - 1)\\
= &(1 - 1) \times N - \sum^{1-1}_{u=0}u + 1 + (4 - 1 - 1)\\
= & 0 - 0 + 1 + 2\\
= &3
\end{aligned}
$$

-   For `i = 2` and `j = 4`

$$
\begin{aligned}
k = &(i - 1) \times N - \sum^{i-1}_{u=0}u + 1 + (j - i - 1)\\
= &(2 - 1) \times N - \sum^{2-1}_{u=0}u + 1 + (4 - 2 - 1)\\
= &N - 1 + 1 + 1\\
= &6
\end{aligned}
$$

-   For `i = 3` and `j = 4`

$$
\begin{aligned}
k = &(i - 1) \times N - \sum^{i-1}_{u=0}u + 1 + (j - i - 1)\\
= &(3 - 1) \times N - \sum^{3-1}_{u=0}u + 1 + (4 - 3 - 1)\\
= &2 \times N - 3 + 1 + 0\\
= &8
\end{aligned}
$$

Therefore, we have the formular for `k` below:

$$
\begin{aligned}
k = &(i - 1) \times N - \sum^{i-1}_{u=0}u + 1 + (j - i - 1)\\
= &(i - 1) \times N - \sum^{i-1}_{u=0}u + j - i
\end{aligned}
$$

Where `i`,`j` (`i < j`) are the two cities where we need to get the distance, and `N` is the total number of cities.

2. Combinations where `i == j` are not valid because the distance from a point to itself does not exist.
3. The formula for how many distances need to be stored is

$$
C^{2}_{n}
$$

\pagebreak

## Problem 4

After these operations:

```python
    Push 1
    Push 2
    Push 3
    Push 4
```

The stack is : `[1, 2, 3, 4]`

After these operations:

```python
    Pop and output the popped item
    Pop and output the popped item
    Push 5
    Push 6
```

The stack is : `[1, 2, 5, 6]`

After these operations:

```python
    Pop and output the popped item
    Pop and output the popped item
    Pop and output the popped item
```

The stack is : `[1]`

#### `<ins>`Answer `</ins>`:

-   At this point there is an underflow on the stack.
-   There is one item left over on the stack which is the element with the value 1.

## Problem 5

The order in which the nodes are visited during a post-order traversal is:

    G - H - D - B - E - I - J - F - C - A

## Problem 6

Pre-order traversal: a b d c e g h f i

In-order traversal: d b a g e h c i f

The tree is built as below:

```python
        a
    b           c
d           e       f
          g   h   i
```

\pagebreak

## Problem 7

Prove

$$
\sum^{n}_{i=1} i = \frac{n(n + 1)}{2}
$$

-   Base case (`n = 1`):

$$
\begin{aligned}
\sum^{1}_{i=1} i &= \frac{1(1 + 1)}{2}\\
&=1
\end{aligned}
$$

-   Assume 𝑃(𝑘) is true for $𝑘 \ge 1$

$$
\begin{aligned}
\sum^{k}_{i=1} i &= \frac{k(k + 1)}{2}\\
\Leftrightarrow 1 + 2 + 3 + \cdots + k &= \frac{k(k + 1)}{2}
\end{aligned}
$$

-   We need to prove

$$
\begin{aligned}
\sum^{k+1}_{i=1} i &= \frac{(k + 1)(k + 2)}{2}\\
\Leftrightarrow 1 + 2 + 3 + \cdots + k + k + 1 &= \frac{(k + 1)(k + 2)}{2}
\end{aligned}
$$

We have

$$
\begin{aligned}
LHS &= \sum^{k+1}_{i=1} i\\
&= \sum^{k}_{i=1} i + k + 1\\
&= \frac{k(k + 1)}{2} + k + 1\\
&= \frac{k(k + 1)}{2} + \frac{2(k + 1)}{2}\\
&= \frac{(k + 1)(k + 2)}{2}\\
&= RHS
\end{aligned}
$$

Therefore, we've proven that

$$
\begin{aligned}
\sum^{k+1}_{i=1} i &= \frac{(k + 1)(k + 2)}{2}\\
\end{aligned}
$$

By mathematical induction, the statement

$$
\sum^{n}_{i=1} i = \frac{n(n + 1)}{2}
$$

is `true` for all $n \ge 1$ and $n \in N$

## Problem 8

Algorithm to build a binary tree from preorder and inorder traversal is illustrated below:

```python
function buildTree(self, preorder, inorder) -> TreeNode:
    if len(preorder) == 0:
        return
    root_val = preorder[0]
    node = new TreeNode(root_val)
    if len(preorder) == 1:
        return node

    root_index = index of root_val in inorder

    // Recursive call in the left subtree
    left_inorder = inorder[0:root_index]
    left_preorder = preorder[1 : 1 + len(left_inorder)]
    node.left = self.buildTree(left_preorder, left_inorder)

    // Recursive call in the right subtree
    right_inorder = inorder[root_index + 1 :]
    right_preorder = preorder[1 + len(left_inorder) :]
    node.right = self.buildTree(right_preorder, right_inorder)

    return node
```

$$
\begin{aligned}
\sum^{n}_{j=i + 1}j = & \sum^{n}_{j=0}j - \sum^{i}_{j=0}j\\
= & \frac{n \times (n+1)}{2} - \frac{i \times (i+1)}{2}\\
\end{aligned}
$$

$$
\begin{aligned}
\sum^{a_{2}}_{i = a_{1}} i = \frac{(a_{1} + a_{2}) \times n}{2}
\end{aligned}
$$

# Homework 1

## Problem 1:

1. The value returned by the function is the variable `r`
2. To find a function of n to express the variable `r`, we need to evaluate the code below:

According to the code

```javascript
    function Algorithm1 (n);
1.      r := 0;
2.      for i := 1 to n-1 do
3.          for j := i + 1 to n do
4.              for k := 1 to j do
5.                  r := r + 1;
6.      return (r );
```

-   In the inner loop:

$$
\begin{aligned}
r = & \sum^{j}_{k=1}1\\
\end{aligned}
$$

-   In the middle loop:

$$
\begin{aligned}
r = & \sum^{n}_{j=i + 1} \sum^{j}_{k=1}1\\
\end{aligned}
$$

-   In the outer loop:

$$
\begin{aligned}
r = &\sum^{n-1}_{i=1} \sum^{n}_{j=i + 1} \sum^{j}_{k=1}1\
\end{aligned}
$$

Therefore, the value `r` is calculated as the function of `n` below

$$
\begin{aligned}
r = &\sum^{n-1}_{i=1} \sum^{n}_{j=i + 1} \sum^{j}_{k=1}1\\
= & \sum^{n-1}_{i=1} \sum^{n}_{j = i + 1}j\\
\end{aligned}
$$

Apply the sum of arithmetic series formular, we have:

$$
\begin{aligned}
\sum^{n-1}_{j = i + 1}j = & \frac{[n - (i + 1) - 1] \times (n + i + 1)}{2}\\
= & \frac{(n - i) \times (n + i + 1)}{2}
\end{aligned}
$$

Therefore, we have the formular of `r` as below:

$$
\begin{aligned}
r = & \sum^{n-1}_{i = 1}\frac{(n - i) \times (n + i + 1)}{2}\\
= & \frac{1}{2}\sum^{n-1}_{i = 1}(n^2 + n -i^2 -i)\\
= & \frac{1}{2}[\sum^{n-1}_{i = 1}(n^2 + n) - \sum^{n-1}_{i = 1}i^2 - \sum^{n-1}_{i = 1}i]\\
\end{aligned}
$$

Apply the sum of square formular, we have:

$$
\begin{aligned}
\sum^{n-1}_{i = 1}i^2 = & \frac{(n-1)(n - 1 + 1)[2(n - 1) + 1]}{6}\\
= & \frac{(n-1)n(2n - 1)}{6}\\
\end{aligned}
$$

Therefore, we have the formular of `r` as below:

$$
\begin{aligned}
r = & \sum^{n-1}_{i = 1}\frac{(n - i) \times (n + i + 1)}{2}\\
= & \frac{1}{2}\sum^{n-1}_{i = 1}(n^2 + n -i^2 -i)\\
= & \frac{1}{2}[\sum^{n-1}_{i = 1}(n^2 + n) - \frac{(n-1)n(2n - 1)}{6} - \sum^{n-1}_{i = 1}i]\\
= & \frac{1}{2}[(n^2 + n)\sum^{n-1}_{i = 1}1 - \frac{(n-1)n(2n - 1)}{6} - \sum^{n-1}_{i = 1}i]\\
= & \frac{1}{2}[(n^2 + n)(n-1) - \frac{(n-1)n(2n - 1)}{6} - \frac{(n-1)n}{2}]\\
= & \frac{1}{2} \times \frac{6(n^2 + n)(n-1) - (n-1)n(2n - 1) - 3(n-1)n}{6}\\
= & \frac{6(n^2 + n)(n-1) - (n-1)n(2n - 1) - 3(n-1)n}{12}\\
= & \frac{(n-1)[6(n^2 + n) - n(2n - 1) - 3n]}{12}\\
= & \frac{(n-1)(6n^2 + 6n - 2n^2 + n - 3n)}{12}\\
= & \frac{(n-1)(4n^2 + 4n)}{12}\\
= & \frac{4(n-1)(n^2 + n)}{12}\\
= & \frac{(n-1)(n^2 + n)}{3}\\
= & \frac{(n-1)n(n + 1)}{3}\\
\end{aligned}
$$

The variable `r` can be expressed in a function of n as illustrated below:

$$
r = \frac{(n-1)n(n + 1)}{3}\\
$$

3. Worst case running time is $O(N^3)$

## Problem 2:

The recursive version of insertion sort works as follows:

1. Recursively sort the subarray `A[1 : n − 1]`
2. Insert the n-th element `A[n]` into the sorted subarray `A[1 : n − 1]`.

We have the time analysis as below:

1. Recursive call: Time to sort the subarray `A[1 : n − 1]` is `T(n-1)`
2. Insertion step: Time to insert the `A[n]` element to the sorted subarray `A[1 : n − 1]` is in the range `[1 : n - 1]`

    - Best case: The time needed is 1
    - Best case: The time needed is n - 1 (insert the `A[n]` elemet to the begining of the sorted subarray `A[1 : n − 1]`)

    => Therefore, we have the time needed is `O(n - 1)`

Therefore, we have the time for recurrence relation for the worst-case running time T(n) can be written as:

$$
T(n) = T(n-1) + O(n)
$$

We have the base case `T(1) = 1`, since the array only have 1 element, the time needed is `O(1)`.

After iteration, we have:

$$
\begin{aligned}
T(n) = & T(n-1) + O(n)\\
= & T(n-2) + O(n -1) + O(n)\\
= & \cdots\\
= & T(1) + O(2) + O(3) + \cdots + O(n)\\
= & O(1) + O(2) + O(3) + \cdots + O(n)\\
= & O(\frac{n(n+1)}{2})\\
= & O(\frac{n^2+n)}{2})\\
= & O(n^2)\\
\end{aligned}
$$

Therefore, the worst-case running time of the recursive version of insertion sort is

$$
T(n)=O(n^2)
$$

## Problem 3:

Pseudocode for the recursive version of the Insertion Sort algorithm:

Base case: Array has only one element

Step 1: Recursively sort the subarray `A[1 : n - 1]`

Step 2: Insert the `n` element to the sorted subarray `A[1 : n - 1]`

We have the following pseudocode as illustrated below:

```javascript
def recursive_insertion_sort(A, n): // A's indices start from 1
    // Base case: if size of subarray is 1
    if n <= 1:
        return

    // Step 1: Recursively sort the array
    recursive_insertion_sort(A, n)

    // Step 2: Insert the n element into the sorted subarray A[1 : n-1]
    key = A[n]

    // Index of the last element in the sorted subarray
    j = n - 1

    while j >= 1 and A[j] > key:
        // Shift A[i] to the right
        A[j + 1] = A[j]
        // Move to the previous element
        j -= 1

    // Insert the element into its correct position in the sorted subarray
    A[j + 1] = key
```

## Problem 4:

To develop an algorithm to linearly sort an array, we need to evaluate the example below:

```javascript
A = [4, 2, 8, 7, 1, 3]
The largest element of array A = 8
```

`<ins>`Step 1 `</ins>`: Create a dictionary `B` in the form of an array with the size equals to the largest element in A, each element in `B` contains a binary value of `0` or `1`.

-   If `B[i] = 0` means the array `A` does not have the value of `i`.
-   Otherwise, if `B[i] = 1` means the value `i` exists in the array `A`.

Therefore, we have the dictionary `B` below:

```javascript
  i  1  2  3  4  5  6  7  8
B = [1, 1, 1, 1, 0, 0, 1, 1]
```

-   `B[1] = 1` because the element `1` exists in `A`.
-   `B[5] = 0` and `B[6] = 0` because the element `5` and `6` does not exist in `A`.

`<ins>`Step 2 `</ins>`: We traverse the dictionary `B` from `i = 1 -> 8` and add `B[i]` to the output arrary if `B[i] == 1`, we have the following order:

```javascript
              i  1  2  3  4  5  6  7  8
            B = [1, 1, 1, 1, 0, 0, 1, 1]
output_array  = [1, 2, 3, 4, 7, 8]
```

Therefore, we have the following pseudocode below:

```javascript
function get_max(A : array) { // A's indices start from 1
    max = -inftyity
    for x in A {
        if x > max {
            max = x
        }
    }
    return max
}

function sort_linear(A : array) {
    max = get_max(A) // get the largest element in A
    B = [0] * (max + 1)

    // Build the dictionary
    for num in A {
        B[num] = 1
    }

    // Traverse the dictionary and return the value
    j = 1
    for i in B {
        if B[i] == 1:
            A[j] = i
            j += 1
    }

    return A
}
```

As a side note, for the above sorting algorithm being effective, the value range of the elements in the array (the number of possible value of all elements in the array) `A` should be relatively small.

## Problem 5:

Pseudocode for binary search

Base case: if `A.length <= 0`, return `key` not found

`<ins>`Step 1 `</ins>`: Find the `mid` point of the array `A`

`<ins>`Step 2 `</ins>`: Assess if `A[mid] == key`

-   if `True`, return `mid` which is the index of the `key` in the array `A`
-   if `False`, move to `Step 3`

`<ins>`Step 3 `</ins>`: Recursively search the array

-   if `A[mid] > key` recursive call on the left partition
    -   `Binary_Search(A[1 : mid - 1])`
-   if `A[mid] < key` recursive call on the right partition
    -   `Binary_Search(A[mid + 1 : A.length])`

```javascript
function Recursive(A, key, low, high) {
    // Base case:
    if low > high
        return -1 // key not found

    // Step 1: calculate the mid point
    mid = math.floor((low + high) / 2)

    if A[mid] == key // Step 2: assess A[mid] == key
        return mid
    else if A[mid] < key // Step 3: recursive call on left partition
        return Recursive(A, key, mid + 1, high)
    else // Step 3: recursive call on right partition
        return Recursive(A, key, low, mid - 1)
}

function BinarySearch(A : array, key) { // A's indices start from 1
    return Recursive(A, key, 1, A.length)
}
```

## Problem 6:

#### `<ins>`Problem 6.a `</ins>`:

From the formula 3.24 in the textbook, we have:

$$
\begin{aligned}
\lg^k n = o(n^\epsilon)
\end{aligned}
$$

Since $\lg^k n = o(n^\epsilon)$, we have the conclusion as below:

$$
\begin{aligned}
\implies &
\begin{cases}
\lg^k n & \text{ is } & O(n^\epsilon)\\
\lg^k n & \text{ is } & o(n^\epsilon)\\
\lg^k n & \text{ is not } & \Omega(n^\epsilon)\\
\lg^k n & \text{ is not } & \omega(n^\epsilon)\\
\lg^k n & \text{ is not } & \Theta(n^\epsilon)\\
\end{cases}
\end{aligned}
$$

#### `<ins>`Problem 6.b `</ins>`:

From the formula 3.13 in the textbook, we have:

$$
\begin{aligned}
n^k = & o(c^n)\\
\end{aligned}
$$

Since $n^k = o(c^n)$, we have the conclusion as below:

$$
\begin{aligned}
\implies &
\begin{cases}
n^k & \text{ is } & O(c^n)\\
n^k & \text{ is } & o(c^n)\\
n^k & \text{ is not } & \Omega(c^n)\\
n^k & \text{ is not } & \omega(c^n)\\
n^k & \text{ is not } & \Theta(c^n)\\
\end{cases}
\end{aligned}
$$

#### `<ins>`Problem 6.c `</ins>`:

To calculate the relative asymptotic growth rates, we are going to calculate the limit below

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{\sqrt{n}}{n^{\sin{n}}}\\
    = & \lim_{n \to \infty} \frac{n^{1/2}}{n^{\sin{n}}}\\
    = & \lim_{n \to \infty} n^{\frac{1}{2}-\sin{n}}\\
\end{aligned}
$$

The sine function, $\sin{n}$, oscillates between − 1 and 1 for all real n. This implies that $sin{n}$ does not converge to a single value as $n \to \infty$

-   When $\sin n = 1$

$$
\begin{aligned}
    & \lim_{n \to \infty} n^{\frac{1}{2}-\sin{n}}\\
    = & \lim_{n \to \infty} n^{\frac{1}{2}-1}\\
    = & \lim_{n \to \infty} n^{\frac{-1}{2}}\\
    = & \lim_{n \to \infty} {\frac{1}{n^\frac{1}{2}}}\\
    = & \lim_{n \to \infty} {\frac{1}{\sqrt{n}}}\\
    = & 0
\end{aligned}
$$

-   When $\sin n = -1$

$$
\begin{aligned}
    & \lim_{n \to \infty} n^{\frac{1}{2}-\sin{n}}\\
    = & \lim_{n \to \infty} n^{\frac{1}{2}-(-1)}\\
    = & \lim_{n \to \infty} n^{\frac{3}{2}}\\
    = & \infty
\end{aligned}
$$

Therefore, the $\lim_{n \to \infty} n^{\frac{1}{2}-\sin{n}}$ does not exist.

Therefore, we have the following conclusion:

$$
\begin{aligned}
\implies &
\begin{cases}
\sqrt{n} & \text{ is not } & O(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \Omega(n^{\sin n})\\
\sqrt{n} & \text{ is not } & o(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \omega(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \Theta(n^{\sin n})\\
\end{cases}
\end{aligned}
$$

#### `<ins>`Problem 6.d `</ins>`:

To calculate the relative asymptotic growth rates, we are going to calculate the limit below

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{2^n}{2^{n/2}}\\
   = & \lim_{n \to \infty} 2^{n - n/2}\\
   = & \lim_{n \to \infty} 2^{n/2}\\
   = & \infty\\
   \implies & 2^n = \omega(2^{n/2})
\end{aligned}
$$

Since $2^n = \omega(2^{n/2})$, we have the conclusion as below:

$$
\begin{aligned}
\implies &
\begin{cases}
n^{\lg c} & \text{ is not } & O(c^{\lg n})\\
n^{\lg c} & \text{ is not } & o(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Omega(c^{\lg n})\\
n^{\lg c} & \text{ is } & \omega(c^{\lg n})\\
n^{\lg c} & \text{ is not } & \Theta(c^{\lg n})\\
\end{cases}
\end{aligned}
$$

#### `<ins>`Problem 6.e `</ins>`:

To calculate the relative asymptotic growth rates, we are going to calculate the limit below

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{n^{\lg c}}{c^{\lg n}}\\
    = & \lim_{n \to \infty} \frac{2^{\lg n \cdot \lg c}}{2^{\lg c \cdot \lg n}}\\
    = & 1 \text{ (constant)}\\
    \implies & n^{\lg c} = \Theta(c^{\lg n})
\end{aligned}
$$

Since $n^{\lg c} = \Theta(c^{\lg n})$, we have the conclusion as below:

$$
\begin{aligned}
\implies &
\begin{cases}
n^{\lg c} & \text{ is } & O(c^{\lg n})\\
n^{\lg c} & \text{ is not } & o(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Omega(c^{\lg n})\\
n^{\lg c} & \text{ is not } & \omega(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Theta(c^{\lg n})\\
\end{cases}
\end{aligned}
$$

#### `<ins>`Problem 6.f `</ins>`:

From the formula 3.28 in the textbook, we have:

$$
\begin{aligned}
lg(n!) = & \Theta(nlg(n))\\
\implies lg(n!) = & \Theta(lg(n^n))
\end{aligned}
$$

Since $lg(n!) = \Theta(lg(n^n))$, we have the conclusion as below:

$$
\begin{aligned}
\implies &
\begin{cases}
lg(n!) & \text{ is } & O(lg(n^n))\\
lg(n!) & \text{ is not } & o(lg(n^n))\\
lg(n!) & \text{ is } & \Omega(lg(n^n))\\
lg(n!) & \text{ is not } & \omega(lg(n^n))\\
lg(n!) & \text{ is } & \Theta(lg(n^n))\\
\end{cases}
\end{aligned}
$$

Therefore, we completed the table as below:

|      | A            | B              | O   | o   | $\Omega$ | $\omega$ | $\Theta$ |
| ---- | ------------ | -------------- | --- | --- | -------- | -------- | -------- |
| $a.$ | $\lg^{k}n$   | $n^{\epsilon}$ | Yes | Yes | No       | No       | No       |
| $b.$ | $n^k$        | $c^n$          | Yes | Yes | No       | No       | No       |
| $c.$ | $\sqrt{n}$   | $n^{\sin{n}}$  | No  | No  | No       | No       | No       |
| $d.$ | $2^n$        | $2^{n/2}$      | No  | No  | Yes      | Yes      | No       |
| $e.$ | $n^{\lg{c}}$ | $c^{\lg{n}}$   | Yes | No  | Yes      | No       | Yes      |
| $f.$ | $\lg(n!)$    | $\lg(n^n)$     | Yes | No  | Yes      | No       | Yes      |

$$
\begin{aligned}
    a^{log_a x} = & x\\
    2^{lg x} = & x\\
    n^{\lg c} = & 2^{(\lg n) \cdot \lg c}\\
    2^{(\lg n) \cdot \lg c} = & 2^{\lg (n^{\lg c})}\\
    \lg (n) \cdot \lg (c) = & \lg (n^{\lg c})
\end{aligned}
$$

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

## Problem 2:

We analyze the time complexity step by step:

-   Outer loop:

The outer loop starts with `i = n` and continues while `i >= 1`, with `i` being halved at each step (`i = ⌊i/2⌋`).

This halving means that the number of iterations of the outer loop is $\lg 𝑛$ because the value of i decreases as $n, n/2, n/4, \cdots, 1$. ⁡

-   Inner loop:

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

## Problem 3:

Given the array

```javascript
   i  1   2   3   4   5   6   7    8    9
A = [12, 34, 37, 45, 57, 82, 95, 100, 134]

target = 100
```

-   `<ins>`Step 1 `</ins>`:

Find the mid point $\frac{1 + 9}{2} = 5$

-   `<ins>`Step 2 `</ins>`:

Since `A[5] != 100` and `A[5] < 100`, we recursively search in the subaray `A[6 : 9]`.

-   Repeat `<ins>`Step 1 `</ins>`:

Find the mid point $\lfloor\frac{6 + 9}{2}\rfloor = 7$

-   Repeat `<ins>`Step 2 `</ins>`:

Since `A[7] != 100` and `A[7] < 100`, we recursively search in the subaray `A[8 : 9]`.

-   Repeat `<ins>`Step 1 `</ins>`:

Find the mid point $\lfloor\frac{8 + 9}{2}\rfloor = 8$

-   Repeat `<ins>`Step 2 `</ins>`:

Since `A[8] == 100`, we terminate and return 8.

## Problem 4:

a.

Given the list as illustrated below:

```javascript
   i   1   2    3   4    5   6  7    9
A = [123, 34, 189, 56, 150, 12, 9, 240]
```

-   `<ins>`Step 1 `</ins>`: Calculate mid piont by the following function:

$$
\begin{aligned}
    mid = &\frac{right - left}{2}\\
    = &\frac{9 - 1}{2}\\
    = &4
\end{aligned}
$$

-   `<ins>`Step 2 `</ins>`:

Devide the array `A` into 2 subarrays

-   Array `B` is `[left, mid]`

```javascript
   i   1   2    3   4
B = [123, 34, 189, 56]
```

-   Array `C` is `[mid, right]`

```javascript
   i   5   6  7    9
C = [150, 12, 9, 240]
```

-   `<ins>`Step 3 `</ins>`:

Repeat `<ins>`Step 1 `</ins>` and `<ins>`Step 2 `</ins>` for subarray `B` and `C`

The array `B` will be halved into array `D` and `E` as illustrated below:

```javascript
   i   1   2    3   4
B = [123, 34, 189, 56]
```

mid =

```javascript
D = [];
```

Repeat until array size is 1

-   `<ins>`Step 4 `</ins>`:

Merge subarrays into the orignal array `A`

We merge these pairs of subarrays together:

-   `[123]` and `[34]` becomes `[34, 123]`
-   `[189]` and `[56]` becomes `[56, 189]`
-   `[150]` and `[12]` becomes `[12, 150]`
-   `[9]` and `[240]` becomes `[9, 240]`

Then we continue to merge these pairs of subarrays together:

-   `[34, 123]` and `[56, 189]` becomes `[34, 56, 123, 189]`
-   `[12, 150]` and `[9, 240]` becomes `[9, 12, 150, 240]`

Then we continue to merge this pairs of subarrays together:

-   `[34, 56, 123, 189]` and `[9, 12, 150, 240]` becomes `[9, 12, 34, 56, 123, 150, 189 240]`

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

## Problem 6:

Pseudocode for ternary search

Base case: if `A.length <= 0`, return `key` not found

`<ins>`Step 1 `</ins>`: Find the `one_third` and `two_thirds` point of the array `A`

`<ins>`Step 2 `</ins>`: Assess if `A[one_third] == key`

-   If `True`, return `one_third` which is the index of the `key` in the array `A`
-   Else if `False`, assess if `A[two_thirds] == key`
-   Else if `True`, return `two_thirds` which is the index of the `key` in the array `A`
-   Else if `False`, move to `Step 3`

`<ins>`Step 3 `</ins>`: Recursively search the array

-   if `A[one_third] > key` recursive call on the left partition
    -   `Ternary_Search(A[1 : one_third - 1])`
-   if `A[two_thirds] > key` and `A[one_third] < key` recursive call on the middle partition
    -   `Ternary_Search(A[one_third + 1 : two_thirds - 1])`
-   if `A[two_thirds] < key` recursive call on the right partition
    -   `Ternary_Search(A[two_thirds + 1 : A.length])`

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

# Homework 3

## Problem 1:

Given a list of n distinct positive integers, rearrange the list into two sublists, each of size n/2, such that the difference between the sums of the integers in the two sublists is maximized.

### Solution:

`<ins>`Step 1:`</ins>` Select a pivot using median of three elements.

`<ins>`Step 2:`</ins>` Partition the subarray around the pivot. All elemenets less than pivot go to the left subarray and all elements greater than pivot go to the right subarray.

`<ins>`Step 3:`</ins>` After the partition step, the pivot will be at its position in the sorted array.

-   If the index of the pivot is less than `n//2`:

    -   Recursively call the function (repeat `<ins>`Step 1 `</ins>` to `<ins>`Step 3 `</ins>`) on the right subarray `A[pivot+1:]`.

-   If the index of the pivot is greater than `n//2`:

    -   Recursively call the function (repeat `<ins>`Step 1 `</ins>` to `<ins>`Step 3 `</ins>`) on the left subarray `A[:pivot]`.

-   If the pivot is at position `n//2`, then the left subarray and right subarray will have `n//2` elements each such that the difference between the sums of the integers in the two sublists is maximized because all `n//2th` largest elements are on the right side and all `n//2th` smallest elements are on the left side.

Recurrence relation:

$$
T(n) = T(n/2) + \Theta(n)
$$

We have:

$$
\begin{aligned}
    f(n) & = n\\
    ws(n) & = n^{\log_{2} 1} = n^0 = 1
\end{aligned}
$$

We have:

$$
\lim_{x \to \infty} \frac{f(n)}{ws(n)} = \frac{n}{1} = n\\
$$

Since $f(n)$ dominates $ws(n)$ by a pollynomial factor, we have:

$$
\begin{aligned}
    & \implies f(n) = \Omega(ws(n) \cdot n^\epsilon) \text{, where } \epsilon > 0\\
    & \implies T(n) = \Theta(f(n)) = \Theta(n)
\end{aligned}
$$

As compared to sorting the array completely approach, this approach is more efficient as it only sorts the half of the array in each recursive call. Therefore, we can say that the time complexity of this approach is better than the sorting the array completely approach.

As a side note, there is linear sorting algorithm called counting sort that can sort the array in linear time, but it is not a comparison-based sorting algorithm and it has some limitations such as it can only sort integers in a specific range or alphabets characters.

/pagebreak

## Problem 2:

```javascript
A = [
        [2, 1],
        [4, 2],
    ]

B = [
        [3, 4],
        [7, 5],
    ]

S1  = B12 - B22         = 4 - 5            = -1
S2  = A11 + A12         = 2 + 1            = 3
S3  = A21 + A22         = 4 + 2            = 6
S4  = B21 - B11         = 7 - 3            = 4
S5  = A11 + A22         = 2 + 2            = 4
S6  = B11 + B22         = 3 + 5            = 8
S7  = A12 - A22         = 1 - 2            = -1
S8  = B21 + B22         = 7 + 5            = 12
S9  = A11 - A21         = 2 - 4            = -2
S10 = B11 + B12         = 3 + 4            = 7

P1  = S1 * A11          = 2 * -1           = -2
P2  = S2 * B22          = 3 * 5            = 15
P3  = S3 * B11          = 6 * 3            = 18
P4  = S4 * A22          = 4 * 2            = 8
P5  = S5 * S6           = 4 * 8            = 32
P6  = S7 * S8           = -1 * 12          = -12
P7  = S9 * S10          = -2 * 7           = -14

C11 = P5 + P4 + P6 - P2 = 32 + 8 - 12 - 15 = 13
C12 = P1 + P2           = -2 + 15          = 13
C21 = P3 + P4           = 18 + 8           = 26
C22 = P5 + P1 - P3 - P7 = 32 - 2 - 18 + 14 = 26

C = [
        [13, 13],
        [26, 26],
    ]
```

/pagebreak

## Problem 3:

We have two $n \times n$ matrices, where $n$ is not a power of 2. We add $c$, where $c > 0$, rows and columns filled with zeros to the two $n \times n$ such that the size of the new matrices is $k \times k$, where $k$ is a power of 2.

We use the Strassen's algorithm to multiply these two $k \times k$ matrices.

Recurrence relation:

$$
T(k) = 7T(k/2) + \Theta(k^2)
$$

We have the solution:

$$
T(k) = \Theta(k^{log_2 7})
$$

Since $k = n + c$, we have

$$
\begin{aligned}
    T(k) = T(n + c) & = \Theta((n + c)^{log_2 7})\\
\end{aligned}
$$

Since $c$ is to some extent a constant, and even if we consider $c$ as a variable, $n$ still grows faster than $c$, $n+c \approx n$. Therefore, we can approximate $n+c$ by $n$ for $n$ approach to inftyity.

In conclusion, for large $n$:

$$
\begin{aligned}
    T(n) = T(n + c) = T(k) = \Theta((n)^{log_2 7})
\end{aligned}
$$

Therefore, the run time is $T(n) = \Theta(n^{log_2 7})$, which does not change when n is not a power of 2.

In the other hand, we try to prove that $n^{\lg 7}$ is $\Theta(\left[n + c\right]^{\lg 7})$.

We have:

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{n^{\lg 7}}{\left[n+c\right]^{\lg 7}}\\
    = & \lim_{n \to \infty} \left[\frac{n}{n+c}\right]^{\lg 7}\\
    = & \lim_{n \to \infty} \left[1 + \frac{n}{c}\right]^{\lg 7}\\
    = & \infty
\end{aligned}
$$

Since $n$ grows way faster than $c$, $\frac{n}{c}$ approaches inftyity as $n$ approaches inftyity. Therefore, the limit is inftyity.

Therefore, we have $n^{\lg 7}$ is $\Theta(\left[n + c\right]^{\lg 7})$.

Therefore, we have $T(n) = \Theta(n^{\lg 7})$.

/pagebreak

## Problem 4:

Show how the Heapsort algorithm works on the following numbers. Show the binary tree view after each step of Build-Max-Heap, and for the rest of Heapsort.

```javascript
A = [60,30,50,80,10,70,40,90,20,100]
n = 10

Parent(i) = floor(i/2)
Left(i) = 2i
Right(i) = 2i + 1

Max-Heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= heap-size[A] and A[l] > A[i]:
        largest = l
        else largest = i
    if r <= heap-size[A] and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange A[i] with A[largest]
        Max-Heapify(A, largest)

Buil-Max-Heap(A, n):
    for i = floor(n/2) to 1:
        Max-Heapify(A, i)

Heap-Sort(A, n):
    Build-Max-Heap(A, n)
    for i = n to 2:
        exchange A[1] with A[i]
        heap-size[A] = heap-size[A] - 1
        Max-Heapify(A, 1)

Build-Max-Heap:
A = [60,30,50,80,10,70,40,90,20,100]
                60
        30              50
    80      10      70      40
  90  20  100

Max-Heapify(A, i=5)
A = [60, 30, 50, 80, 100, 70, 40, 90, 20, 10]
                60
        30              50
    80      100     70      40
  90  20  10

Max-Heapify(A, i=10)
A = [60, 30, 50, 80, 100, 70, 40, 90, 20, 10]
                60
        30              50
    80      100     70      40
  90  20  10

Max-Heapify(A, i=4)
A = [60, 30, 50, 90, 100, 70, 40, 80, 20, 10]
                60
        30              50
    90      100     70      40
  80  20  10

Max-Heapify(A, i=8)
A = [60, 30, 50, 90, 100, 70, 40, 80, 20, 10]
                60
        30              50
    90      100     70      40
  80  20  10

Max-Heapify(A, i=3)
A = [60, 30, 70, 90, 100, 50, 40, 80, 20, 10]
                60
        30              70
    90      100     50      40
  80  20  10

Max-Heapify(A, i=6)
A = [60, 30, 70, 90, 100, 50, 40, 80, 20, 10]
                60
        30              70
    90      100     50      40
  80  20  10

Max-Heapify(A, i=2)
A = [60, 100, 70, 90, 30, 50, 40, 80, 20, 10]
                60
        100             70
    90      30      50      40
  80  20  10

Max-Heapify(A, i=5)
A = [60, 100, 70, 90, 30, 50, 40, 80, 20, 10]
                60
        100             70
    90      30      50      40
  80  20  10

Max-Heapify(A, i=1)
A = [100, 60, 70, 80, 30, 50, 40, 90, 20, 10]
                100
        60              70
    90      30      50      40
  80  20  10

Max-Heapify(A, i=2)
A = [100, 60, 70, 90, 30, 50, 40, 80, 20, 10]
                100
        90              70
    60      30      50      40
  80  20  10

Max-Heapify(A, i=4)
A = [100, 90, 70, 60, 30, 50, 40, 80, 20, 10]
                100
        90              70
    60      30      50      40
  80  20  10

Max-Heapify(A, i=8)
A = [100, 90, 70, 80, 30, 50, 40, 60, 20, 10]
                100
        90              70
    80      30      50      40
  60  20  10

Remove 100 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 9
A = [10, 90, 70, 80, 30, 50, 40, 60, 20, 100]
                10
        90              70
    80      30      50      40
  60  20

Max-Heapify(A, i=1)
A = [90, 10, 70, 80, 30, 50, 40, 60, 20, 100]
                90
        10              70
    80      30      50      40
  60  20

Max-Heapify(A, i=2)
A = [90, 80, 70, 10, 30, 50, 40, 60, 20, 100]
                90
        80              70
    10      30      50      40
  60  20

Max-Heapify(A, i=4)
A = [90, 80, 70, 60, 30, 50, 40, 10, 20, 100]
                90
        80              70
    60      30      50      40
  10  20

Max-Heapify(A, i=8)
A = [90, 80, 70, 60, 30, 50, 40, 10, 20, 100]
                90
        80              70
    60      30      50      40
  10  20

Remove 90 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 8
A = [20, 80, 70, 60, 30, 50, 40, 10, 90, 100]
                20
        80              70
    60      30      50      40
  10

Max-Heapify(A, i=1)
A = [80, 20, 70, 60, 30, 50, 40, 10, 90, 100]
                80
        20              70
    60      30      50      40
  10

Max-Heapify(A, i=2)
A = [80, 60, 70, 20, 30, 50, 40, 10, 90, 100]
                80
        60              70
    20      30      50      40
  10

Max-Heapify(A, i=4)
A = [80, 60, 70, 20, 30, 50, 40, 10, 90, 100]
                80
        60              70
    20      30      50      40
  10

Max-Heapify(A, i=8)
A = [80, 60, 70, 20, 30, 50, 40, 10, 90, 100]
                80
        60              70
    20      30      50      40
  10

Remove 80 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 7
A = [10, 60, 70, 20, 30, 50, 40, 80, 90, 100]
                10
        60              70
    20      30      50      40

Max-Heapify(A, i=1)
A = [70, 60, 10, 20, 30, 50, 40, 80, 90, 100] 3
                70
        60              10
    20      30      50      40

Max-Heapify(A, i=3)
A = [70, 60, 50, 20, 30, 10, 40, 80, 90, 100] 6
                70
        60              50
    20      30      10      40

Max-Heapify(A, i=6)
A = [70, 60, 50, 20, 30, 10, 40, 80, 90, 100] 6
                70
        60              50
    20      30      10      40

Remove 70 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 6
A = [40, 60, 50, 20, 30, 10, 70, 80, 90, 100]
                40
        60              50
    20      30      10

Max-Heapify(A, i=1)
A = [60, 40, 50, 20, 30, 10, 70, 80, 90, 100]
                60
        40              50
    20      30      10

Max-Heapify(A, i=2)
A = [60, 40, 50, 20, 30, 10, 70, 80, 90, 100]
                60
        40              50
    20      30      10

Remove 60 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 5
A = [10, 40, 50, 20, 30, 60, 70, 80, 90, 100]
                10
        40              50
    20      30

Max-Heapify(A, i=1)
A = [50, 40, 10, 20, 30, 60, 70, 80, 90, 100]
                50
        40              10
    20      30

Max-Heapify(A, i=3)
A = [50, 40, 10, 20, 30, 60, 70, 80, 90, 100]
                50
        40              10
    20      30

Remove 50 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 4
A = [30, 40, 10, 20, 50, 60, 70, 80, 90, 100]
                30
        40              10
    20

Max-Heapify(A, i=1)
A = [40, 30, 10, 20, 50, 60, 70, 80, 90, 100]
                40
        30              10
    20

Max-Heapify(A, i=2)
A = [40, 30, 10, 20, 50, 60, 70, 80, 90, 100]
                40
        30              10
    20

Remove 40 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 3
A = [20, 30, 10, 40, 50, 60, 70, 80, 90, 100]
                20
        30              10

Max-Heapify(A, i=1)
A = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100]
                30
        20              10

Max-Heapify(A, i=2)
A = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100]
                30
        20              10

Remove 30 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 2
A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                10
        20

Max-Heapify(A, i=1)
A = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100]
                20
        10
Remove 20 (swap with last element and heapify)
Heap-Size = Heap-Size - 1 = 1
A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                10

Heap-Size = 1 (only one element left)
=> Terminate
```

\pagebreak

## Problem 5:

Draw binary search trees of height 2, 3, 4, 5, and 6 from the set of keys {1, 4, 5, 10, 16, 17, 21}

#### Binary Search Trees of height 2

```javascript
            10
           /  \
         4      17
        / \    /  \
       1   5 16   21
```

#### Binary Search Trees of height 3

```javascript
            10
           /  \
         5      17
        /      /  \
       4     16   21
      /
     1
```

#### Binary Search Trees of height 4

```javascript
            16
           /  \
         10     17
        /         \
       5          21
      /
     4
    /
   1
```

#### Binary Search Trees of height 5

```javascript
           17
          /  \
        16    21
       /
      10
     /
    5
   /
  4
 /
1
```

#### Binary Search Trees of height 6

```javascript
21 / 17 / 16 / 10 / 5 / 4 / 1;
```

\pagebreak

## Problem 6:

Suppose `c` and `k` are positive constants such that `1 < c < k`. Is $c^n$ little-o, $\Theta$, or little-$\omega$ of $k^n$?

We have:

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{c^n}{k^n}\\
    = & \lim_{n \to \infty} \left(\frac{c}{k}\right)^n\\
\end{aligned}
$$

Since:

$$
\begin{aligned}
& 1 < c < k\\
\implies & 0 < \frac{c}{k} < 1\\
\implies & \lim_{n \to \infty} \left(\frac{c}{k}\right)^n = 0\\
\end{aligned}
$$

Therefore, we have:

$$
\begin{aligned}
c^n & \text{ is } & o(n^k)\\
c^n & \text{ is not } & \omega(n^k)\\
c^n & \text{ is not } & \Theta(n^k)\\
\end{aligned}
$$

Suppose `c` and `k` are positive constants such that `1 < c < k`. Is $\ln c^n$ little-o, $\Theta$, or little-$\omega$ of $\ln k^n$?

We have:

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{\ln c^n}{\ln k^n}\\
    = & \lim_{n \to \infty} \frac{n\ln c}{n\ln k}\\
    = & \lim_{n \to \infty} \frac{\ln c}{\ln k}\\
    = & \frac{\ln c}{\ln k}\\
\end{aligned}
$$

Therefore, we have:

$$
\begin{aligned}
\lg c^n & \text{ is not} & o(\lg k^n)\\
\lg c^n & \text{ is not } & \omega(\lg k^n)\\
\lg c^n & \text{ is } & \Theta(\lg k^n)\\
\end{aligned}
$$

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

## Problem 3:

Modify MEMOIZED-CUT-ROD to return not only the value but the actual solution, too

```javascript
def MEMOIZED-CUT-ROD-MODIFIED(p: list[int], l: int, memo:dict = {}, sol:dict = {}) -> (int, list[int]):
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

## Problem 4:

```javascript
   i 0  1   2  3  4   5
p = [2, 3, 10, 5, 4, 20];

```

## The Table

| i \ j | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 60=2x3x10`<br>`size=2x10`<br>`s=1`<br>`seq=1 | 160=min(60+2x10x5,`<br>`150+2x3x5)`<br>`size=2x5`<br>`s=2`<br>`seq=5 | 200=min(160+2x5x4,`<br>`210+2x3x4,`<br>`60+200+2x10x4)`<br>`size=2x4`<br>`s=3`<br>`seq=8 | 360=min(200+2x4x20,`<br>`450+2x3x20,`<br>`160+400+2x5x20,`<br>`60+1000+2x10x20)`<br>`size=2x20`<br>`s=4`<br>`seq=10 |
| 2 | 0 | 0 | 150=3x10x5`<br>`size=3x5`<br>`s=2`<br>`seq=2 | 210=min(150+3x5x4,`<br>`200+3x10x4)`<br>`size=3x4`<br>`s=3`<br>`seq=6 | 450=min(210+3x4x20,`<br>`1000+3x10x20,`<br>`150+400+3x520)`<br>`size=3x20`<br>`s=4`<br>`seq=9 |
| 3 | 0 | 0 | 0 | 200=10x5x4`<br>`size=10x4`<br>`s=3`<br>`seq=3 | 1000=min(200+10x4x20,`<br>`400+10x5x20)`<br>`size=10x20`<br>`s=4`<br>`seq=7 |
| 4 | 0 | 0 | 0 | 0 | 400=5x4x20`<br>`size=5x20`<br>`s=4`<br>`seq=4 |
| 5 | 0 | 0 | 0 | 0 | 0 |

The optimal parenthesis is:

`((((A1.A2).A3).A4).A5)`

P = [3, 4, 5, 1, 2]

M =

| i \ j | 1   | 2                 | 3                                                       | 4                                                                         |
| ----- | --- | ----------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1     | 0   | 3x4x5=60<br />3x5 | min(60+3x5x1,<br />20+3x4x1)<br />=32<br />4x1<br />s=1 | min(64+5x2x3,<br />48+5x4x3,<br />60+18+5x3x3)<br />=94<br />5x3<br />s=3 |
| 2     | 0   | 0                 | 4x5x1=20<br />4x1                                       | min(24+4x2x3,<br />18+4x3x3)<br />=48<br />4x3<br />s=3                   |
| 3     | 0   | 0                 | 0                                                       | 5x1x2=10<br />5x2                                                         |
| 4     | 0   | 0                 | 0                                                       | 0                                                                         |

$$
\begin{aligned}
    & T(n) = 3T(n/2) + \Theta(n)\\
    & f(n) = n\\
    & ws(n) = n^{\log_{2} 3}\\
    & \lim_{n \to \infty} \frac{f(n)}{ws(n)}\\
    & = \lim_{n \to \infty} \frac{n}{n^{\log_{2} 3}}\\
    & = \lim_{n \to \infty} n^{1 - \log_{2} 3}\\
\end{aligned}
$$

we have:

$$
\begin{aligned}
    & \log_{2} 2 - \log_{2} 3 < 0\\
    & \text{There exists at least 1 } \epsilon \text{ where: }\\
    & 1 - \log_{2} 3 + \epsilon < 0\\
    & \implies \lim_{n \to \infty} n^{1 - \log_{2} 3 + \epsilon} = 0 \\
    & \implies f(n) = O(\frac{ws(n)}{n^{\epsilon}})\\
    & \implies T(n) = \Theta(ws(n)) = \Theta(n^{\log_{2} 3})\\
\end{aligned}
$$

p = [5, 3, 6, 7, 8, 1, 2 , 4, 9]

# Homework 5:

## Problem 1:

For the fractional knapsack problem, since we could take a part of the metal, we could take the most valuable metal first before taking other less valuable metals without the need of reconsidering previous decisions. For that reason, the fractional knapsack problem satisfy the greedy-choice property. As compared to binary knapsack problem, we couldn't simply take the most valuable metal as we might end up not fully ultilizing our capacity where selecting a combination of cheaper metals might results in a better total value. Therefore, the binary knapsack problem does not satisfy the greedy-choice property.

## Problem 2:

Given the following frequency table as below:

|                          | a   | b     | c    | d    | e   | f   | g    | h   | i   | j     |
| ------------------------ | --- | ----- | ---- | ---- | --- | --- | ---- | --- | --- | ----- |
| Frequency                | 10  | 2     | 4    | 5    | 15  | 9   | 6    | 8   | 12  | 1     |
| Variable-length codeword | 101 | 00001 | 0001 | 1100 | 01  | 100 | 1101 | 001 | 111 | 00000 |

## Problem 3:

### a

| Vertices | d        | $\pi$ |
| -------- | -------- | ----- |
| 1        | $\infty$ | None  |
| 2        | 3        | 4     |
| 3        | 0        | None  |
| 4        | 2        | 5     |
| 5        | 1        | 3     |
| 6        | 1        | 3     |

### b

| Vertices | d   | $\pi$ |
| -------- | --- | ----- |
| r        | 4   | s     |
| s        | 3   | w     |
| t        | 1   | u     |
| u        | 0   | None  |
| v        | 5   | r     |
| w        | 2   | t     |
| x        | 1   | u     |
| y        | 1   | u     |

## Problem 4:

### Prim's Algorithm

| Vertices | d | $\pi$ | Set S |
| --- | --- | --- | --- |
| 1 | 0 | None | [1] |
| 2 | $\infty$ -> 4 | None -> 1 | [1] |
| 3 | $\infty$ -> 2 | None -> 1 | [1] |
| 4 | $\infty$ -> 6 -> 5 -> 4 -> 3 | None -> 1 -> 2 -> 5 -> 6 | [1] -> [1,3,2] <br />->[1,3,2,5]<br />-> [1,3,2,5,6] |
| 5 | $\infty$ -> 3 | None -> 2 | [1,3,2] |
| 6 | $\infty$ -> 1 | None -> 5 | [1,3,2,5] |
| 7 | $\infty$ -> 10 -> 2 | None -> 3 -> 9 | [1,3]<br />-> [1,3,2,5,6,9] |
| 8 | $\infty$ -> 8 -> 5 -> 2 | None -> 5 -> 6 -> 9 | [1,3,2,5]<br />-> [1,3,2,5,6]<br />-> [1,3,2,5,6,9] |
| 9 | $\infty$ -> 2 | None -> 6 | [1,3,2,5,6] |
| 10 | $\infty$ -> 7 -> 3 | None -> 6 -> 9 | [1,3,2,5,6]<br />-> [1,3,2,5,6,9]<br />-> [1,3,2,5,6,9,7]<br />-> [1,3,2,5,6,9,7,8]<br />-> [1,3,2,5,6,9,7,8,4]<br />-> [1,3,2,5,6,9,7,8,4,10] |

### Kruskal's Algorithm

| Edges   | Weight | Add to MST | Parent array                       |
| ------- | ------ | ---------- | ---------------------------------- |
| (5, 6 ) | 1      | Yes        | [0, 1, 2, 3, 4, 6, 6, 7, 8, 9, 10] |
| (1, 3 ) | 2      | Yes        | [0, 3, 2, 3, 4, 6, 6, 7, 8, 9, 10] |
| (6, 9 ) | 2      | Yes        | [0, 3, 2, 3, 4, 6, 6, 7, 8, 6, 10] |
| (7, 9 ) | 2      | Yes        | [0, 3, 2, 3, 4, 6, 6, 6, 8, 6, 10] |
| (8, 9 ) | 2      | Yes        | [0, 3, 2, 3, 4, 6, 6, 6, 6, 6, 10] |
| (2, 5 ) | 3      | Yes        | [0, 3, 6, 3, 4, 6, 6, 6, 6, 6, 10] |
| (4, 6 ) | 3      | Yes        | [0, 3, 6, 3, 6, 6, 6, 6, 6, 6, 10] |
| (9, 10) | 3      | Yes        | [0, 3, 6, 3, 6, 6, 6, 6, 6, 6, 6]  |
| (1, 2 ) | 4      | Yes        | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (4, 5 ) | 4      | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (2, 4 ) | 5      | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (6, 8 ) | 5      | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (1, 4 ) | 6      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (8, 10) | 6      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (4, 7 ) | 7      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (6, 10) | 7      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (3, 4 ) | 8      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (5, 8 ) | 8      | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (3, 7 ) | 10     | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |

## Problem 5:

### a

Vertex `s` as the source

| Vertices | d              | $\pi$       | Set S                                                                          |
| -------- | -------------- | ----------- | ------------------------------------------------------------------------------ |
| s        | 0              | None        | [`s`]                                                                          |
| t        | $\infty$ -> 3  | None -> `s` | [`s`]                                                                          |
| x        | $\infty$ -> 9  | None -> `t` | [`s`, `t`]                                                                     |
| y        | $\infty$ -> 5  | None -> `s` | [`s`]                                                                          |
| z        | $\infty$ -> 11 | None -> `y` | [`s`, `t`, `y`]<br />-> [`s`, `t`, `y`, `x`]<br />-> [`s`, `t`, `y`, `x`, `z`] |

### b

Vertex `z` as the source

| Vertices | d             | $\pi$       | Set S                                                                                             |
| -------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------- |
| s        | $\infty$ -> 3 | None -> `z` | [`z`]                                                                                             |
| t        | $\infty$ -> 6 | None -> `s` | [`z`, `s`]                                                                                        |
| x        | $\infty$ -> 7 | None -> `z` | [`z`]                                                                                             |
| y        | $\infty$ -> 8 | None -> `s` | [`z`, `s`]<br />-> [`z`, `s`, `t`]<br />-> [`z`, `s`, `t`, `x`]<br />-> [`z`, `s`, `t`, `x`, `y`] |
| z        | 0             | None        | [`z`]                                                                                             |
