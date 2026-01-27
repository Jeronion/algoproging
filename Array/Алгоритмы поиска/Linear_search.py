from math import *
from bisect import *
from heapq import *
from collections import *
from itertools import *
from time import *
from sys import *

from typing import (
    List,
    Optional,
    Dict,
    Set,
    Tuple,
    Deque,
    DefaultDict,
    Any,
    Callable,
    Iterable,
)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=223#1
def informatics_223():
    L = int(input())
    array = map(int, input().split())
    N = int(input())

    c = 0
    for i in array:
        if i == N:
            c += 1

    print(c)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=224#1
def informatics_224():
    L = int(input())
    array = map(int, input().split())
    N = int(input())

    for i in array:
        if i == N:
            print("YES")
            break
    else:
        print("NO")


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=225#1
def informatics_225():
    L = int(input())
    array = map(int, input().split())
    N = int(input())

    nearest = float("inf")
    for i in array:
        if abs(N - i) < abs(N - nearest):
            nearest = i

    print(nearest)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=226#1
def informatics_226():
    L = int(input())
    array = list(map(int, input().split()))
    N = int(input())

    for i in range(L):
        if array[i] == N:
            print(i + 1, "")


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=227#1
def informatics_227():
    N = int(input())
    array = map(int, input().split())

    m = float("-inf")
    for i in array:
        if i > m:
            m = i

    print(m)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=228#1
def informatics_228():
    N = int(input())
    array = list(map(int, input().split()))

    m = 0
    for i in range(N):
        if array[i] > array[m]:
            m = i

    print(m + 1)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=1409#1
def informatics_1409():
    N = int(input())
    array = map(int, input().split())

    ms = [float("inf"), float("inf")]
    for i in array:
        if i <= ms[0]:
            ms[0], ms[1] = i, ms[0]
        elif i <= ms[1]:
            ms[1] = i

    print(*ms)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=1412#1
def informatics_1412():
    X = int(input())
    L = int(input())
    result = ["NO"] * L

    for _ in range(L):
        row = map(int, input().split())
        i = 0
        for j in row:
            if j == X:
                result[i] = "YES"
            i += 1

    print(*result, sep="\n")


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=1427#1
def informatics_1427():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    row_min = [min(row) for row in matrix]
    col_max = [max(matrix[i][j] for i in range(n)) for j in range(m)]

    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                result += 1

    print(result)


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=1440#1
def informatics_1440():
    N = int(input())
    M = map(int, input().split())

    mins = [float("-inf"), float("-inf")]
    for i in M:
        if i > mins[0]:
            mins[0], mins[1] = i, mins[0]
        elif i > mins[1] and i != mins[0]:
            mins[1] = i

    print(mins[1])


# https://informatics.msk.ru/mod/statements/view.php?id=270&chapterid=1447#1
def informatics_1447():
    data = map(int, input().split())
    N = next(data)
    array = list(data)

    mn = min(array)
    mx = max(array)

    print(*map(lambda x: mn if x == mx else x, array))
