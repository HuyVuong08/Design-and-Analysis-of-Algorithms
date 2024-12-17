
# Homework 2

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

* In the inner loop:
$$
\begin{aligned}
r = & \sum^{j}_{k=1}1\\
\end{aligned}
$$

* In the middle loop:
$$
\begin{aligned}
r = & \sum^{n}_{j=i + 1} \sum^{j}_{k=1}1\\
\end{aligned}
$$

* In the outer loop:
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

Apply  the sum of square formular, we have:
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

\pagebreak

## Problem 2:

The recursive version of insertion sort works as follows:

1. Recursively sort the subarray `A[1 : n − 1]`
2. Insert the n-th element `A[n]` into the sorted subarray `A[1 : n − 1]`.

We have the time analysis as below:
1. Recursive call: Time to sort the subarray `A[1 : n − 1]` is `T(n-1)`
2. Insertion step: Time to insert the `A[n]` element to the sorted subarray `A[1 : n − 1]` is in the range `[1 : n - 1]`
   * Best case: The time needed is 1
   * Best case: The time needed is n - 1 (insert the `A[n]` elemet to the begining of the sorted subarray `A[1 : n − 1]`)
   
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

\pagebreak

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

\pagebreak

## Problem 4:

To develop an algorithm to linearly sort an array, we need to evaluate the example below:

```javascript
A = [4, 2, 8, 7, 1, 3]
The largest element of array A = 8
```

<ins>Step 1</ins>: Create a dictionary `B` in the form of an array with the size equals to the largest element in A, each element in `B` contains a binary value of `0` or `1`.

* If `B[i] = 0` means the array `A` does not have the value of `i`. 
* Otherwise, if `B[i] = 1` means the value `i` exists in the array `A`.

Therefore, we have the dictionary `B` below:
```javascript
  i  1  2  3  4  5  6  7  8
B = [1, 1, 1, 1, 0, 0, 1, 1]
```

* `B[1] = 1` because the element `1` exists in `A`.
* `B[5] = 0` and `B[6] = 0` because the element `5` and `6` does not exist in `A`.

<ins>Step 2</ins>: We traverse the dictionary `B` from `i = 1 -> 8` and add `B[i]` to the output arrary if `B[i] == 1`, we have the following order:

```javascript
              i  1  2  3  4  5  6  7  8
            B = [1, 1, 1, 1, 0, 0, 1, 1]
output_array  = [1, 2, 3, 4, 7, 8]
```

After these two steps, the time complexity is O(n)

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

In conclusion, to sort an array using this algorithm, the worst case in running time is O(n) 

As a side note, for the above sorting algorithm being effective, the value range of the elements in the array (the number of possible value of all elements in the array) `A` should be relatively small.

\pagebreak

## Problem 5:

Pseudocode for binary search

Base case: if `A.length <= 0`, return `key` not found

<ins>Step 1</ins>: Find the `mid` point of the array `A`

<ins>Step 2</ins>: Assess if `A[mid] == key`

* if `True`, return `mid` which is the index of the `key` in the array `A`
* if `False`, move to `Step 3`

<ins>Step 3</ins>: Recursively search the array

* if `A[mid] > key` recursive call on the left partition
    * `Binary_Search(A[1 : mid - 1])`
* if `A[mid] < key` recursive call on the right partition
    * `Binary_Search(A[mid + 1 : A.length])`

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
To determine whether the element exists in the array, we must continue to halve the search interval until the size of the interval is 1. Therefore, in both best case and worst case, the running time will also be $\lg n$

Therefore, we have:
$$
\begin{aligned}
    \text{Worst case: } O(\lg n)\\
    \text{Best case: } \Omega(\lg n)\\
\end{aligned}
$$

Therefore, the running time for binary search is $\Theta(\lg n)$

\pagebreak

## Problem 6:

#### <ins>Problem 6.a</ins>:

From the formula 3.24 in the textbook, we have:
$$
\begin{aligned}
\lg^k n = o(n^\epsilon)
\end{aligned}
$$

Since $\lg^k n = o(n^\epsilon)$, we have the conclusion as below:

$$
\begin{aligned}
\lg^k n & \text{ is } & O(n^\epsilon)\\
\lg^k n & \text{ is } & o(n^\epsilon)\\
\lg^k n & \text{ is not } & \Omega(n^\epsilon)\\
\lg^k n & \text{ is not } & \omega(n^\epsilon)\\
\lg^k n & \text{ is not } & \Theta(n^\epsilon)\\
\end{aligned}
$$

#### <ins>Problem 6.b</ins>:

From the formula 3.13 in the textbook, we have:
$$
\begin{aligned}
n^k = & o(c^n)\\
\end{aligned}
$$

Since $n^k = o(c^n)$, we have the conclusion as below:

$$
\begin{aligned}
n^k & \text{ is } & O(c^n)\\
n^k & \text{ is } & o(c^n)\\
n^k & \text{ is not } & \Omega(c^n)\\
n^k & \text{ is not } & \omega(c^n)\\
n^k & \text{ is not } & \Theta(c^n)\\
\end{aligned}
$$

#### <ins>Problem 6.c</ins>:

To calculate the relative asymptotic growth rates, we are going to calculate the limit below

$$
\begin{aligned}
    & \lim_{n \to \infty} \frac{\sqrt{n}}{n^{\sin{n}}}\\
    = & \lim_{n \to \infty} \frac{n^{1/2}}{n^{\sin{n}}}\\
    = & \lim_{n \to \infty} n^{\frac{1}{2}-\sin{n}}\\
\end{aligned}
$$

The sine function, $\sin{n}$, oscillates between − 1 and 1 for all real n. This implies that $sin{n}$ does not converge to a single value as $n \to \infty$

* When $\sin n = 1$ 
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

* When $\sin n = -1$ 
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
\sqrt{n} & \text{ is not } & O(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \Omega(n^{\sin n})\\
\sqrt{n} & \text{ is not } & o(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \omega(n^{\sin n})\\
\sqrt{n} & \text{ is not } & \Theta(n^{\sin n})\\
\end{aligned}
$$

#### <ins>Problem 6.d</ins>:

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
n^{\lg c} & \text{ is not } & O(c^{\lg n})\\
n^{\lg c} & \text{ is not } & o(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Omega(c^{\lg n})\\
n^{\lg c} & \text{ is } & \omega(c^{\lg n})\\
n^{\lg c} & \text{ is not } & \Theta(c^{\lg n})\\
\end{aligned}
$$

#### <ins>Problem 6.e</ins>:

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
n^{\lg c} & \text{ is } & O(c^{\lg n})\\
n^{\lg c} & \text{ is not } & o(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Omega(c^{\lg n})\\
n^{\lg c} & \text{ is not } & \omega(c^{\lg n})\\
n^{\lg c} & \text{ is } & \Theta(c^{\lg n})\\
\end{aligned}
$$

#### <ins>Problem 6.f</ins>:

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
lg(n!) & \text{ is } & O(lg(n^n))\\
lg(n!) & \text{ is not } & o(lg(n^n))\\
lg(n!) & \text{ is } & \Omega(lg(n^n))\\
lg(n!) & \text{ is not } & \omega(lg(n^n))\\
lg(n!) & \text{ is } & \Theta(lg(n^n))\\
\end{aligned}
$$

Therefore, we completed the table as below:

| | A| B| O | o | $\Omega$ | $\omega$ | $\Theta$ |
| -|-|-|-|-|-|-|-|
| $a.$| $\lg^{k}n$| $n^{\epsilon}$| Yes| Yes| No| No| No|
| $b.$| $n^k$| $c^n$| Yes| Yes| No| No| No|
| $c.$| $\sqrt{n}$| $n^{\sin{n}}$| No| No| No| No| No|
| $d.$| $2^n$| $2^{n/2}$| No| No| Yes| Yes| No|
| $e.$| $n^{\lg{c}}$| $c^{\lg{n}}$| Yes| No| Yes| No| Yes|
| $f.$| $\lg(n!)$| $\lg(n^n)$| Yes| No| Yes| No| Yes|
