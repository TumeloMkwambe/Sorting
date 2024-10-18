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
    runtimes = list()
    for i in range(100, 10100, 1000):
        runtimes.append([i, timer(bubble_sort, generator(i))])
    return runtimes

def test_bubble_clause():
    runtimes = list()
    for i in range(100, 10100, 1000):
        runtimes.append([i, timer(bubble_sort_clause, generator(i))])
    return runtimes

def save(array, sort):
    np.savetxt(sort, array, delimiter=',', header="input,time")


save(test_bubble(), "bubble_sort.csv")
save(test_bubble_clause(), "bubble_sort_clause.csv")