import numpy as np


def select_sort(l):
    N = len(l)
    for i in range(N):
        min = i
        for j in range(i + 1, N):
            if l[j] < l[min]:
                min = j
        t = l[i]
        l[i] = l[min]
        l[min] = t


L = np.random.permutation(100)
print(L)
print('-' * 64)
select_sort(L)
print(L)
