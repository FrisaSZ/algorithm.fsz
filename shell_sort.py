import numpy as np


def shell_sort(l):
    N = len(l)
    h = 1
    h_list = []
    while h < N // 3:
        h_list.append(h)
        h = 3 * h + 1
    print(h_list)
    h_list = h_list[::-1]
    for h_ in h_list:
        for i in range(h_, N):
            j = i
            while j >= h_ and l[j] < l[j - h_]:
                t = l[j - h_]
                l[j - h_] = l[j]
                l[j] = t
                j -= h_


L = np.random.permutation(1000)
print(L)
print('-' * 64)
shell_sort(L)
print(L)
