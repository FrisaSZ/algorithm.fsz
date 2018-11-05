import numpy as np


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
