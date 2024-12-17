# Homework 3

## Problem 1:

Given a list of n distinct positive integers, rearrange the list into
two sublists, each of size n/2, such that the difference between the sums of the integers in the two sublists is
maximized.

### Solution:

<ins>Step 1:</ins> Select a pivot using median of three elements.

<ins>Step 2:</ins> Partition the subarray around the pivot. All elemenets less than pivot go to the left subarray and all elements greater than pivot go to the right subarray.

<ins>Step 3:</ins> After the partition step, the pivot will be at its position in the sorted array. 

- If the index of the pivot is less than `n//2`:
  - Recursively call the function (repeat <ins>Step 1</ins> to <ins>Step 3</ins>) on the right subarray `A[pivot+1:]`.
- If the index of the pivot is greater than `n//2`:
  - Recursively call the function (repeat <ins>Step 1</ins> to <ins>Step 3</ins>) on the left subarray `A[:pivot]`.

- If the pivot is at position `n//2`, then the left subarray and right subarray will have `n//2` elements each such that the difference between the sums of the integers in the two sublists is maximized because all `n//2th` largest elements are on the right side and all `n//2th` smallest elements are on the left side.

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

\pagebreak

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

\pagebreak

## Problem 3:

We have two $n \times n$ matrices, where $n$ is not a power of 2.  We add $c$, where $c > 0$, rows and columns filled with zeros to the two $n \times n$ such that the size of the new matrices is $k \times k$, where $k$ is a power of 2. 

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

Since $c$ is to some extent a constant, and even if we consider $c$ as a variable, $n$ still grows faster than $c$, $n+c \approx n$. Therefore, we can approximate $n+c$ by  $n$ for  $n$ approach to inftyity.

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
    = \infty
\end{aligned}
$$

Since $n$ grows way faster than $c$, $\frac{n}{c}$ approaches inftyity as $n$ approaches inftyity. Therefore, the limit is inftyity.

Therefore, we have $n^{\lg 7}$ is $\Theta(\left[n + c\right]^{\lg 7})$.

Therefore, we have $T(n) = \Theta(n^{\lg 7})$.

\pagebreak

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
n = 10
      0  1  2  3  4  5  6  7  8   9
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
             21
            /
           17
          /
        16
       /
      10
     /
    5
   /
  4
 /
1
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
