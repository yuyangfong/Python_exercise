
# coding: utf-8

# Bubble Sort, Reverse = True則大至小(預設值)；反之小至大

def bubble_sort_fun(x, reverse = 1):
    for i in range(0, len(x) - 1):
        for j in range(i + 1, len(x)):
            if reverse == 0:
                if x[i] > x[j]:
                    x[i], x[j] = x[j], x[i]
            elif reverse == 1:
                if x[i] < x[j]:
                    x[i], x[j] = x[j], x[i]
    return x

import random
lst = random.sample(range(0, 100), 20)
print('亂數數列:', lst, sep = '\n')
print('排序數列(大至小):', exchange_sort(lst, reverse = 1), sep = '\n')
print('排序數列(小至大):', exchange_sort(lst, reverse = 0), sep = '\n')

