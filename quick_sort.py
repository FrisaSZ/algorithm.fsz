import numpy as np
import time


def exchange(l, i, j):
    t = l[i]
    l[i] = l[j]
    l[j] = t


def partition(l, lo, hi):
    v = l[lo]
    i = lo
    j = hi + 1  # 避免 j 首次递减把 hi 给略过了
    while True:
        while True:
            i += 1
            if l[i] >= v or i == hi:
                break
        while True:
            j -= 1
            if l[j] <= v or j == lo:  # j == lo 是冗余判断，因为当 j 到了 lo 时，会因为 l[lo] <= v而跳出循环
                break
        if i >= j:
            break
        exchange(l, i, j)
    exchange(l, lo, j)
    return j


def quick_sort(l, lo, hi):
    if lo >= hi:
        return
    j = partition(l, lo, hi)
    quick_sort(l, lo, j - 1)
    quick_sort(l, j + 1, hi)


L = np.random.permutation(1000000)
print(L)
print('-' * 64)
start = time.time()
quick_sort(L, 0, len(L) - 1)
duration = time.time() - start
print('time cost {}'.format(duration))
print(L)
