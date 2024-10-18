import sys
import math
import time
import random
import numpy as np


def generator(n):
    List = list()
    i = 0
    while len(List) != n:
        entry = random.randint(0, n**2)
        if entry not in List:
            List.append(entry)
            i = i + 1
    return List

def bubble_sort(array):
    for i in range(len(array), 0, -1):
        for j in  range(i - 1):
            if(array[j] > array[j+1]):
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
    return array

def bubble_sort_clause(array):
    i = len(array)
    sorting = True
    while (i >= 1 and sorting == True):
        swopped = False
        for j in range(i - 1):
            if(array[j] > array[j+1]):
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
                swopped = True
        if swopped == False:
            sorting = False
        else:
            i -= 1
    return array

import math

def merge_sort(array, left, right):
    if right - left > 0:
        mid = (left + right) // 2

        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)

        merge(array, left, mid, right)

def merge(array, left, mid, right):

    left_array = array[left:mid + 1]
    right_array = array[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

def timer(function, array):
    start = time.time()
    function(array)
    stop = time.time() - start
    return stop

def merge_timer(array):
    start = time.time()
    merge_sort(array, 0, len(array) - 1)
    stop = time.time() - start
    return stop

def test_bubble():
    bubble_runtimes = list()
    bubble_clause_best_runtimes = list()
    bubble_clause_worst_runtimes = list()
    merge_runtimes = list()
    for i in range(100, 10100, 1000):
        array = generator(i)
        bubble_runtimes.append([i, timer(bubble_sort, array)]) # test bubble sort without clause
        merge_runtimes.append([i, merge_timer(array)])
        array.sort()
        bubble_clause_best_runtimes.append([i, timer(bubble_sort_clause, array)]) # best case: list is already sorted
        array.sort(reverse=True)
        bubble_clause_worst_runtimes.append([i, timer(bubble_sort_clause, array)]) # worst case : list is sorted in reverse
    return bubble_runtimes, bubble_clause_best_runtimes, bubble_clause_worst_runtimes, merge_runtimes

def save(array, sort):
    np.savetxt(sort, array, delimiter=',', header="input,time")

bubble_runtimes, bubble_clause_best_runtimes, bubble_clause_worst_runtimes, merge_runtimes = test_bubble()

save(bubble_runtimes, "bubble_sort.csv")
save(bubble_clause_best_runtimes, "bubble_clause_best.csv")
save(bubble_clause_worst_runtimes, "bubble_clause_worst.csv")
save(merge_runtimes, "merge_sort.csv")
