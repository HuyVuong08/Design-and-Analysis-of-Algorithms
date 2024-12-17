## I did the quick sort with median of three pivot selection strategy

## Address the stack overflow by increasing the recursion limit

```python

sys.setrecursionlimit(10000)

```

## Runs showing output

![List of runs](list.png)

## A table of time and #comparisons for all algorithms for all sizes for each type of data.

![Table of Actual Performance](table.png)

| Sort Algorithm        | Input Type | Input Size | Runtime (ms) | Number of Comparisons |
| :-------------------- | :--------- | ---------: | -----------: | --------------------: |
| Bubble Sort           | Random     |       1000 |      52.1243 |                496068 |
| Bubble Sort           | Random     |       2000 |      200.512 |               1982878 |
| Bubble Sort           | Random     |       4000 |      820.165 |               7992719 |
| Bubble Sort           | Random     |       8000 |      3262.49 |              31959888 |
| Bubble Sort           | Sorted     |       1000 |    0.0650883 |                   999 |
| Bubble Sort           | Sorted     |       2000 |     0.126839 |                  1999 |
| Bubble Sort           | Sorted     |       4000 |     0.256062 |                  3999 |
| Bubble Sort           | Sorted     |       8000 |     0.520945 |                  7999 |
| Bubble Sort           | Reversed   |       1000 |       62.562 |                499500 |
| Bubble Sort           | Reversed   |       2000 |       257.21 |               1999000 |
| Bubble Sort           | Reversed   |       4000 |       999.51 |               7998000 |
| Bubble Sort           | Reversed   |       8000 |      4118.78 |              31996000 |
| Insertion Sort        | Random     |       1000 |      22.1102 |                250725 |
| Insertion Sort        | Random     |       2000 |       86.936 |                982151 |
| Insertion Sort        | Random     |       4000 |      352.779 |               3931875 |
| Insertion Sort        | Random     |       8000 |      1425.06 |              15829989 |
| Insertion Sort        | Sorted     |       1000 |     0.108004 |                   999 |
| Insertion Sort        | Sorted     |       2000 |     0.215054 |                  1999 |
| Insertion Sort        | Sorted     |       4000 |     0.430107 |                  3999 |
| Insertion Sort        | Sorted     |       8000 |     0.859261 |                  7999 |
| Insertion Sort        | Reversed   |       1000 |       43.189 |                499500 |
| Insertion Sort        | Reversed   |       2000 |      175.706 |               1999000 |
| Insertion Sort        | Reversed   |       4000 |      711.633 |               7998000 |
| Insertion Sort        | Reversed   |       8000 |      2863.63 |              31996000 |
| Quick Sort Randomized | Random     |       1000 |       1.4379 |                 10680 |
| Quick Sort Randomized | Random     |       2000 |      3.02482 |                 23458 |
| Quick Sort Randomized | Random     |       4000 |      6.48403 |                 52135 |
| Quick Sort Randomized | Random     |       8000 |      14.3123 |                119643 |
| Quick Sort Randomized | Sorted     |       1000 |      54.3752 |                499500 |
| Quick Sort Randomized | Sorted     |       2000 |      221.766 |               1999000 |
| Quick Sort Randomized | Sorted     |       4000 |      889.186 |               7998000 |
| Quick Sort Randomized | Sorted     |       8000 |      3569.74 |              31996000 |
| Quick Sort Randomized | Reversed   |       1000 |      43.3168 |                499500 |
| Quick Sort Randomized | Reversed   |       2000 |       170.67 |               1991836 |
| Quick Sort Randomized | Reversed   |       4000 |      688.094 |               7972388 |
| Quick Sort Randomized | Reversed   |       8000 |      2741.99 |              31862194 |
| Quick Sort Median     | Random     |       1000 |      1.56593 |                 12394 |
| Quick Sort Median     | Random     |       2000 |      3.29089 |                 26757 |
| Quick Sort Median     | Random     |       4000 |      7.66683 |                 61593 |
| Quick Sort Median     | Random     |       8000 |      14.8051 |                125032 |
| Quick Sort Median     | Sorted     |       1000 |      1.38211 |                 10988 |
| Quick Sort Median     | Sorted     |       2000 |       2.8801 |                 23964 |
| Quick Sort Median     | Sorted     |       4000 |      6.13999 |                 51920 |
| Quick Sort Median     | Sorted     |       8000 |      13.1121 |                111841 |
| Quick Sort Median     | Reversed   |       1000 |      1.95527 |                 17205 |
| Quick Sort Median     | Reversed   |       2000 |      4.34995 |                 38878 |
| Quick Sort Median     | Reversed   |       4000 |      9.77397 |                 87302 |
| Quick Sort Median     | Reversed   |       8000 |      20.9479 |                194622 |
| Heap Sort             | Random     |       1000 |      2.86102 |                 16924 |
| Heap Sort             | Random     |       2000 |      6.46472 |                 37675 |
| Heap Sort             | Random     |       4000 |      14.2481 |                 83408 |
| Heap Sort             | Random     |       8000 |      31.2939 |                182964 |
| Heap Sort             | Sorted     |       1000 |      3.10397 |                 17583 |
| Heap Sort             | Sorted     |       2000 |      6.73604 |                 39160 |
| Heap Sort             | Sorted     |       4000 |      14.8749 |                 86580 |
| Heap Sort             | Sorted     |       8000 |      33.0729 |                189418 |
| Heap Sort             | Reversed   |       1000 |      2.64788 |                 15965 |
| Heap Sort             | Reversed   |       2000 |      5.85389 |                 35964 |
| Heap Sort             | Reversed   |       4000 |       13.454 |                 80147 |
| Heap Sort             | Reversed   |       8000 |      48.4841 |                176052 |
| 3-Way Merge Sort      | Random     |       1000 |      1.95312 |                  9020 |
| 3-Way Merge Sort      | Random     |       2000 |      4.49991 |                 20223 |
| 3-Way Merge Sort      | Random     |       4000 |      9.49001 |                 44563 |
| 3-Way Merge Sort      | Random     |       8000 |      21.3881 |                 97741 |
| 3-Way Merge Sort      | Sorted     |       1000 |      1.37281 |                  5970 |
| 3-Way Merge Sort      | Sorted     |       2000 |      3.34215 |                 13541 |
| 3-Way Merge Sort      | Sorted     |       4000 |      5.99408 |                 29085 |
| 3-Way Merge Sort      | Sorted     |       8000 |      14.0748 |                 63225 |
| 3-Way Merge Sort      | Reversed   |       1000 |      1.13797 |                  4381 |
| 3-Way Merge Sort      | Reversed   |       2000 |      2.56991 |                  9433 |
| 3-Way Merge Sort      | Reversed   |       4000 |        4.776 |                 20898 |
| 3-Way Merge Sort      | Reversed   |       8000 |      11.4582 |                 45107 |

## Theoretical performance for each case:

| Algorithm             | Best Case Time Complexity | Average Case Time Complexity | Worst Case Time Complexity |
| --------------------- | ------------------------- | ---------------------------- | -------------------------- |
| Bubble Sort           | $\Theta(n)$               | $\Theta(n^2)$                | $\Theta(n^2)$              |
| Insertion Sort        | $\Theta(n)$               | $\Theta(n^2)$                | $\Theta(n^2)$              |
| Quick Sort Randomized | $\Theta(n \log n)$        | $\Theta(n \log n)$           | $\Theta(n^2)$              |
| Quick Sort Median     | $\Theta(n \log n)$        | $\Theta(n \log n)$           | $\Theta(n \log n)$         |
| Heap Sort             | $\Theta(n \log n)$        | $\Theta(n \log n)$           | $\Theta(n \log n)$         |
| 3-Way Merge Sort      | $\Theta(n \log n)$        | $\Theta(n \log n)$           | $\Theta(n \log n)$         |

## Are the theoretical and practical performance results consistent? Any anomalies and/or surprises?

| Algorithm             | Best Case No. Comparisons for `n=8000`  | Average Case No. Comparisons for `n=8000` | Worst Case No. Comparisons for `n=8000` |
| --------------------- | --------------------------------------- | ----------------------------------------- | --------------------------------------- |
| Bubble Sort           | $7,999 \approx 8000^2$                  | $31,985,358 \approx 8000^2$               | $31,996,000 \approx 8000^2$             |
| Insertion Sort        | $7,999 \approx 8000^2$                  | $15,797,394 \approx 8000^2$               | $31,996,000 \approx 8000^2$             |
| Quick Sort Randomized | $128,385 \approx 8000 \times \log 8000$ | $123,118 \approx 8000 \times \log 8000$   | $31,878,438 \approx 8000^2$             |
| Quick Sort Median     | $111,836 \approx 8000 \times \log 8000$ | $132,277 \approx 8000 \times \log 8000$   | $193,831 \approx 8000 \times \log 8000$ |
| Heap Sort             | $189,456 \approx 8000 \times \log 8000$ | $182,821 \approx 8000 \times \log 8000$   | $176,074 \approx 8000 \times \log 8000$ |
| 3-Way Merge Sort      | $63,218 \approx 8000 \times \log 8000$  | $97,724 \approx 8000 \times \log 8000$    | $45,107 \approx 8000 \times \log 8000$  |

#### Consistency Check

- **Bubble Sort**: Theoretical $\Theta(n^2)$ for average and worst cases. Practical results should show quadratic growth in runtime and comparisons.
- **Insertion Sort**: Theoretical $\Theta(n^2)$ for average and worst cases. Practical results should show quadratic growth in runtime and comparisons.
- **Quick Sort Randomized**: Theoretical $\Theta(n \log n)$ for average case and $\Theta(n^2)$ for worst case. Practical results should show near-linearithmic growth in runtime and comparisons for average cases.
- **Quick Sort Median of Three**: Theoretical $\Theta(n \log n)$ for average case and $\Theta(n^2)$ for worst case. Practical results should show near-linearithmic growth in runtime and comparisons for average cases.
- **Heap Sort**: Theoretical $\Theta(n \log n)$ for all cases. Practical results should show linearithmic growth in runtime and comparisons.
- **3-Way Merge Sort**: Theoretical $\Theta(n \log n)$ for all cases. Practical results should show linearithmic growth in runtime and comparisons.

#### Anomalies and Surprises

- **Bubble Sort and Insertion Sort**: In the `sorted` input, these two algorithms perfomed the task in linear time.

- **Quick Sort Randomized**: In the `reversed` and `sorted` input, the `Quick Sort` with `Randomized pivot selection` shows poor performance, which is on par with `Insertion Sort` and `Bubble Sort`.

- **Heap Sort** and **3-Way Merge Sort** **Quick Sort Median of Three** show consistent results with the theoretical $\Theta(n \log n)$ performance in all three types of data input.

- **3-Way Merge Sort** the `random` input case requires more comparisons than the `sorted` input case, but the runtime is shorter for the `random` input case. This is because the `random` input case requires more merging steps, but each merging step is faster.

- **Quick Sort Median of Three** performs consistently well across all input types, confirming that choosing a median pivot helps stabilize performance and avoid worst-case scenarios. The reduced number of comparisons compared to Quick Sort Randomized suggests that the median strategy is more efficient in selecting pivots.

- **Quick Sort Median of Three** and **Heap Sort** have a similar number of comparisons for the three types of input, but the runtime for `Quick Sort Median of Three` is significantly faster. This is because `Quick Sort Median of Three` has a better pivot selection strategy, leading to fewer swaps as compared to `Heap Sort` which requires more swaps to maintain the heap property.

### Analysis and discussion of the results vs expectations

#### Bubble Sort

- **Expected**: $\Theta(n^2)$ for average and worst cases.
- **Observed**: The runtime and comparisons grow quadratically with input size, the results are consistent with expectations. However, a significant deviation towards linear performance in the sorted input data.

#### Insertion Sort

- **Expected**: $\Theta(n^2)$ for average and worst cases.
- **Observed**: Similar to Bubble Sort, quadratic growth in runtime and comparisons in most of the cases. However, a significant deviation towards linear performance in the sorted input data.

#### Quick Sort Randomized

- **Expected**: $\Theta(n \log n)$ for average case, $\Theta(n^2)$ for worst case.
- **Observed**: Near-linearithmic growth in runtime and comparisons for most of the cases. However, a significant deviation towards quadratic performance occured in the sorted data input, which suggests poor pivot selection.

#### Quick Sort Median of Three

- **Expected**: $\Theta(n \log n)$ for average case, $\Theta(n^2)$ for worst case.
- **Observed**: Consistent linearithmic growth in runtime and comparisons for all three types of data input. This suggests that the median-of-three pivot selection strategy is effective in avoiding worst-case scenarios.

#### Heap Sort

- **Expected**: $\Theta(n \log n)$ for all cases.
- **Observed**: Consistent linearithmic growth in runtime and comparisons for all three types of data input.

#### 3-Way Merge Sort

- **Expected**: $\Theta(n \log n)$ for all cases.
- **Observed**: Consistent linearithmic growth in runtime and comparisons for all three types of data input.

#### Quick Sort Randomized vs Quick Sort Median of Three

- **Quick Sort Randomized** shows poor performance in the `reversed` and `sorted` input data, which is expected due to the random pivot selection strategy.
- **Quick Sort Median of Three** performs consistently well across all input types, confirming that choosing a median pivot helps stabilize performance and avoid worst-case scenarios. The reduced number of comparisons compared to Quick Sort Randomized suggests that the median strategy is more efficient in selecting pivots. Quick Sort Median remedied the problem of Quick Sort algorithm by ensuring the pivot is not the smallest or largest element in the array.
