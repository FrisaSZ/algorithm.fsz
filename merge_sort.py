import numpy as np
import time


def merge(l, lo, mid, hi):
    i = lo
    j = mid + 1
    l_aux = l.copy()
    for k in range(lo, hi + 1):
        if i > mid:
            l[k] = l_aux[j]
            j += 1
        elif j > hi:
            l[k] = l_aux[i]
            i += 1
        elif l_aux[i] < l_aux[j]:
            l[k] = l_aux[i]
            i += 1
        else:
            l[k] = l_aux[j]
            j += 1


def top_down_sort(l, lo, hi):
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    top_down_sort(l, lo, mid)
    top_down_sort(l, mid + 1, hi)
    merge(l, lo, mid, hi)


def bottom_up_sort(l):
    N = len(l)
    sz = 1
    while sz < N:
        lo = 0
        while lo < N - sz:
            merge(l, lo, lo + sz - 1, min(lo + 2 * sz - 1, N - 1))
            lo += 2 * sz
        sz += sz


''' 测试merge算法
L = np.random.permutation(100)
left = L[:50]
right = L[50:]
print('-' * 64)
print(left)
print('-' * 64)
print(right)
left.sort()
right.sort()
print('-' * 64)
print(left)
print('-' * 64)
print(right)
L = np.append(left, right)
merge(L, 0, 49, 99)
print(L)
'''

L = np.random.permutation(100000)
L_copy = L.copy()
print(L)
print('-' * 64)
start = time.time()
top_down_sort(L, 0, len(L) - 1)
duration = time.time() - start
print('time cost {}'.format(duration))
print(L)
print('-' * 64)
start = time.time()
bottom_up_sort(L_copy)
duration = time.time() - start
print('time cost {}'.format(duration))
print(L_copy)
