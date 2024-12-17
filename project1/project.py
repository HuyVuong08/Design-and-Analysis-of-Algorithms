import random
import time
import pandas as pd
import numpy as np
import sys

from data_8000 import reverse8

input1 = reverse8.copy()

# Increase the recursion limit
sys.setrecursionlimit(10000)

# Bubble sort algorithm (most efficient version)
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    while n > 1:
        new_n = 0
        for i in range(1, n):
            comparisons += 1
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                new_n = i
        n = new_n
    return comparisons

# Insersion sort algorithm
def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j >= 0:
            comparisons += 1
    return comparisons

# Quick sort algorithm with randomized pivot selection
class Quick_Sort_Randomized:
    def sort(self, arr):
        global comparisons
        comparisons = 0
        self.quick_sort_recursive(arr, 0, len(arr) - 1)
        return comparisons

    def partition(self, arr, low, high):
        global comparisons
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(self, arr, low, high):
        if low > high:
            return
        pi = self.partition(arr, low, high)
        self.quick_sort_recursive(arr, low, pi - 1)
        self.quick_sort_recursive(arr, pi + 1, high)

quick_sort_randomized = Quick_Sort_Randomized()

# Quick sort algorithm with median-of-three pivot selection
class Quick_Sort_Median:
    def sort(self, arr):
        global comparisons
        comparisons = 0
        self.quick_sort_recursive(arr, 0, len(arr) - 1)
        return comparisons

    def median_of_three(self, arr, low, high):
        global comparisons
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        comparisons += 3
        return mid

    def partition(self, arr, low, high):
        global comparisons
        pivot_index = self.median_of_three(arr, low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(self, arr, low, high):
        if low > high:
            return
        pi = self.partition(arr, low, high)
        self.quick_sort_recursive(arr, low, pi - 1)
        self.quick_sort_recursive(arr, pi + 1, high)

quick_sort_median = Quick_Sort_Median()

# Heap sort algorithm
def heapify(arr, n, i):
    if i > n:
        return
    global comparisons
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Compare left child
    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    # Compare right child
    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    global comparisons
    comparisons = 0
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return comparisons

# Merge sort algorithm
class Merge_Sort:
    def sort(self, arr):
        self.comparisons = 0
        arr = self.recursive(arr)
        return self.comparisons

    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def recursive(self, arr):
        if len(arr) <= 1:
            return arr
        if len(arr) == 2:
            self.comparisons += 1
            if arr[0] > arr[1]:
                return [arr[1], arr[0]]
            return arr
        mid1 = len(arr) // 3
        mid2 = 2*len(arr) // 3

        left = self.recursive(arr[:mid1])
        mid = self.recursive(arr[mid1:mid2])
        right = self.recursive(arr[mid2:])
        return self.merge(self.merge(left, mid), right)

merge_sort = Merge_Sort()

class List:
    def __init__(self, type, size, list):
        self.type = type
        self.size = size
        self.list = list

input_data = []

for i in [1000, 2000, 4000, 8000]:
    input_data.append(List("Random", i, [random.randint(1, 1000001) for _ in range(i)]))
length = len(input_data)
for i in range(length):
    input_data.append(List("Sorted", input_data[i].size, sorted(input_data[i].list)))
for i in range(length):
    input_data.append(List("Reversed", input_data[i].size, sorted(input_data[i].list, reverse=True)))

# Extract the three 8000-element datasets
datasets_8000 = [data for data in input_data if data.size == 8000]

# Write the datasets into a .txt file
with open('datasets_8000.txt', 'w') as file:
    for dataset in datasets_8000:
        file.write(f"{dataset.type}:\n")
        file.write(','.join(map(str, dataset.list)) + "\n\n")

dict = {
    'b': {'label': 'Bubble Sort', 'function': bubble_sort},
    'i': {'label': 'Insertion Sort', 'function': insertion_sort},
    'qr': {'label': 'Quick Sort Randomized', 'function': quick_sort_randomized.sort},
    'qm': {'label': 'Quick Sort Median', 'function': quick_sort_median.sort},
    'h': {'label': 'Heap Sort', 'function': heap_sort},
    'm': {'label': '3-Way Merge Sort', 'function': merge_sort.sort},
}

sort_algo, results = ['b', 'i', 'qr', 'qm', 'h', 'm'], []

print('{:>2}.  {:^9}  {:^9} {:^24} {:>12}  {:>16}'.format("No", "Data Type", "Data Size", "Sorting Algorithm", "Elapsed time", "No. Comparisons"))
for s in sort_algo:
    if s not in dict:
        continue
    for data in input_data :
        input = data.list.copy()
        start_time = time.time()
        comparisons = dict[s]['function'](input)
        duration = time.time() - start_time
        line_new = '{:>2}.  {:^9}  {:^9} {:^24} {:>12}  {:>16,}'.format(len(results)+1, data.type, data.size, dict[s]['label'], f'{duration*1000:,.3f} ms', comparisons)
        print(line_new)
        results.append([dict[s]['label'], data.type, len(input), duration * 1000, int(comparisons)])

# Define column names of the data frame
columns = ['Sort Algorithm', 'Input Type', 'Input Size', 'Runtime (ms)', 'Number of Comparisons']

# Create a dataframe
df = pd.DataFrame(results, columns=columns)

# Format the columns to display decimal digits and add thousands separators
df['Input Size'] = df['Input Size'].apply(lambda x: f'{int(x):,}')
df['Number of Comparisons'] = df['Number of Comparisons'].apply(lambda x: f'{int(x):,}')
df['Runtime (ms)'] = df['Runtime (ms)'].apply(lambda x: f'{x:,.3f}')

# Pivot the dataframe to have 'Sort Algorithm' as columns
df = df.pivot(index=['Input Type', 'Input Size'], columns='Sort Algorithm', values=['Runtime (ms)', 'Number of Comparisons'])

# Reorder the columns
order = ['Bubble Sort', 'Insertion Sort', 'Quick Sort Randomized', 'Quick Sort Median', 'Heap Sort', '3-Way Merge Sort']
df = df.reindex(columns=pd.MultiIndex.from_product([['Runtime (ms)', 'Number of Comparisons'], order]))

input_type_order = ['Random', 'Sorted', 'Reversed']
df = df.reindex(input_type_order, level='Input Type')

# Save the dataframe to a CSV and xlsx file
df.to_csv('sort_algorithms.csv')
df.to_excel('sort_algorithms.xlsx')
markdown_table = df.to_markdown(index=False)

print(markdown_table)
print(df)