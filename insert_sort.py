import numpy as np


def insert_sort(l):
    N = len(l)
    for i in range(1, N):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            t = l[j - 1]
            l[j - 1] = l[j]
            l[j] = t
            j -= 1


L = np.random.permutation(1000)
print(L)
print('-' * 64)
insert_sort(L)
print(L)
