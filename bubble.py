import sys
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

def timer(function, array):
    start = time.time()
    function(array)
    stop = time.time() - start
    return stop

def test_bubble():
    bubble_runtimes = list()
    bubble_clause_best_runtimes = list()
    bubble_clause_worst_runtimes = list()
    for i in range(100, 10100, 1000):
        array = generator(i)
        bubble_runtimes.append([i, timer(bubble_sort, array)]) # test bubble sort without clause
        array.sort()
        bubble_clause_best_runtimes.append([i, timer(bubble_sort_clause, array)]) # best case: list is already sorted
        array.sort(reverse=True)
        bubble_clause_worst_runtimes.append([i, timer(bubble_sort_clause, array)]) # worst case : list is sorted in reverse
    return bubble_runtimes, bubble_clause_best_runtimes, bubble_clause_worst_runtimes

def save(array, sort):
    np.savetxt(sort, array, delimiter=',', header="input,time")

bubble_runtimes, bubble_clause_best_runtimes, bubble_clause_worst_runtimes = test_bubble()

save(bubble_runtimes, "bubble_sort.csv")
save(bubble_clause_best_runtimes, "bubble_clause_best.csv")
save(bubble_clause_worst_runtimes, "bubble_clause_worst.csv")