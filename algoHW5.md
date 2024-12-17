# Homework 5:

## Problem 1:

For the fractional knapsack problem, since we could take a part of the metal, we could take the most valuable metal first before taking other less valuable metals without the need of reconsidering previous decisions. For that reason, the fractional knapsack problem satisfy the greedy-choice property. As compared to binary knapsack problem, we couldn't simply take the most valuable metal as we might end up not fully ultilizing our capacity where selecting a combination of cheaper metals might results in a better total value. Therefore, the binary knapsack problem does not satisfy the greedy-choice property.

<div style="page-break-after: always;"></div>

## Problem 2:

Given the following frequency table as below:

|                          | a   | b     | c    | d    | e   | f   | g    | h   | i   | j     |
| ------------------------ | --- | ----- | ---- | ---- | --- | --- | ---- | --- | --- | ----- |
| Frequency                | 10  | 2     | 4    | 5    | 15  | 9   | 6    | 8   | 12  | 1     |
| Variable-length codeword | 101 | 00001 | 0001 | 1100 | 01  | 100 | 1101 | 001 | 111 | 00000 |

Huffman's code tree

```javascript
            (12, 'i')
        (23, 'dgi')
                (6, 'g')
            (11, 'dg')
                (5, 'd')
    (42, 'fadgi')
            (10, 'a')
        (19, 'fa')
            (9, 'f')
(72, 'jbchefadgi')
        (15, 'e')
    (30, 'jbche')
            (8, 'h')
        (15, 'jbch')
                (4, 'c')
            (7, 'jbc')
                    (2, 'b')
                (3, 'jb')
                    (1, 'j')
```

<div style="page-break-after: always;"></div>

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

<div style="page-break-after: always;"></div>

## Problem 4:

### Prim's Algorithm

| Vertices | d                            | $\pi$                    | Order | Set S                                                                                                                                          |
| -------- | ---------------------------- | ------------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | 0                            | None                     | 1     | [1]                                                                                                                                            |
| 2        | $\infty$ -> 4                | None -> 1                | 3     | [1]                                                                                                                                            |
| 3        | $\infty$ -> 2                | None -> 1                | 2     | [1]                                                                                                                                            |
| 4        | $\infty$ -> 6 -> 5 -> 4 -> 3 | None -> 1 -> 2 -> 5 -> 6 | 9     | [1] -> [1,3,2] <br />->[1,3,2,5]<br />-> [1,3,2,5,6]                                                                                           |
| 5        | $\infty$ -> 3                | None -> 2                | 4     | [1,3,2]                                                                                                                                        |
| 6        | $\infty$ -> 1                | None -> 5                | 5     | [1,3,2,5]                                                                                                                                      |
| 7        | $\infty$ -> 10 -> 2          | None -> 3 -> 9           | 7     | [1,3]<br />-> [1,3,2,5,6,9]                                                                                                                    |
| 8        | $\infty$ -> 8 -> 5 -> 2      | None -> 5 -> 6 -> 9      | 8     | [1,3,2,5]<br />-> [1,3,2,5,6]<br />-> [1,3,2,5,6,9]                                                                                            |
| 9        | $\infty$ -> 2                | None -> 6                | 6     | [1,3,2,5,6]                                                                                                                                    |
| 10       | $\infty$ -> 7 -> 3           | None -> 6 -> 9           | 10    | [1,3,2,5,6]<br />-> [1,3,2,5,6,9]<br />-> [1,3,2,5,6,9,7]<br />-> [1,3,2,5,6,9,7,8]<br />-> [1,3,2,5,6,9,7,8,4]<br />-> [1,3,2,5,6,9,7,8,4,10] |

<div style="page-break-after: always;"></div>

### Kruskal's Algorithm

| Edges   | Weight | Order | Add to MST | Parent array                       |
| ------- | ------ | ----- | ---------- | ---------------------------------- |
| (5, 6 ) | 1      | 1     | Yes        | [0, 1, 2, 3, 4, 6, 6, 7, 8, 9, 10] |
| (1, 3 ) | 2      | 2     | Yes        | [0, 3, 2, 3, 4, 6, 6, 7, 8, 9, 10] |
| (6, 9 ) | 2      | 3     | Yes        | [0, 3, 2, 3, 4, 6, 6, 7, 8, 6, 10] |
| (7, 9 ) | 2      | 4     | Yes        | [0, 3, 2, 3, 4, 6, 6, 6, 8, 6, 10] |
| (8, 9 ) | 2      | 5     | Yes        | [0, 3, 2, 3, 4, 6, 6, 6, 6, 6, 10] |
| (2, 5 ) | 3      | 6     | Yes        | [0, 3, 6, 3, 4, 6, 6, 6, 6, 6, 10] |
| (4, 6 ) | 3      | 7     | Yes        | [0, 3, 6, 3, 6, 6, 6, 6, 6, 6, 10] |
| (9, 10) | 3      | 8     | Yes        | [0, 3, 6, 3, 6, 6, 6, 6, 6, 6, 6]  |
| (1, 2 ) | 4      | 9     | Yes        | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (4, 5 ) | 4      | 10    | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (2, 4 ) | 5      | 11    | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (6, 8 ) | 5      | 12    | No         | [0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (1, 4 ) | 6      | 13    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (8, 10) | 6      | 14    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (4, 7 ) | 7      | 15    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (6, 10) | 7      | 16    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (3, 4 ) | 8      | 17    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (5, 8 ) | 8      | 18    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |
| (3, 7 ) | 10     | 19    | No         | [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  |

<div style="page-break-after: always;"></div>

## Problem 5:

### a

Vertex `s` as the source

| Vertices | d              | $\pi$       | Order | Set S                                                                          |
| -------- | -------------- | ----------- | ----- | ------------------------------------------------------------------------------ |
| s        | 0              | None        | 1     | [`s`]                                                                          |
| t        | $\infty$ -> 3  | None -> `s` | 2     | [`s`]                                                                          |
| x        | $\infty$ -> 9  | None -> `t` | 4     | [`s`, `t`]                                                                     |
| y        | $\infty$ -> 5  | None -> `s` | 3     | [`s`]                                                                          |
| z        | $\infty$ -> 11 | None -> `y` | 5     | [`s`, `t`, `y`]<br />-> [`s`, `t`, `y`, `x`]<br />-> [`s`, `t`, `y`, `x`, `z`] |

### b

Vertex `z` as the source

| Vertices | d             | $\pi$       | Order | Set S                                                                                             |
| -------- | ------------- | ----------- | ----- | ------------------------------------------------------------------------------------------------- |
| s        | $\infty$ -> 3 | None -> `z` | 2     | [`z`]                                                                                             |
| t        | $\infty$ -> 6 | None -> `s` | 3     | [`z`, `s`]                                                                                        |
| x        | $\infty$ -> 7 | None -> `z` | 4     | [`z`]                                                                                             |
| y        | $\infty$ -> 8 | None -> `s` | 5     | [`z`, `s`]<br />-> [`z`, `s`, `t`]<br />-> [`z`, `s`, `t`, `x`]<br />-> [`z`, `s`, `t`, `x`, `y`] |
| z        | 0             | None        | 1     | [`z`]                                                                                             |
