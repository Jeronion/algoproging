import sys
import random

# https://informatics.msk.ru/mod/statements/view.php?id=271#1
def solution_271():
    N = int(input())
    arr = list(map(int, input().split()))
    m = 0
    for i in range(1, N):
        if arr[i] > arr[m]:
            m = i
    arr[0], arr[m] = arr[m], arr[0]
    return arr


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=230#1
def solution_230():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=231#1
def solution_231():
    N = int(input())
    arr = list(map(int, input().split())) + [None]
    n, x = map(int, input().split())
    for i in range(x - 1, N):
        n, arr[i] = arr[i], n
    return arr


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=232#1
def solution_232():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=233#1
def solution_233():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        swapped = False
        
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            return arr


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=1411#1
def solution_1411():
    N = int(input())
    arr = list(map(int, input().split()))
    c = 0
    for i in range(N):
        swapped = False
        
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                c += 1
        
        if not swapped:
            return c


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=1426#1
def solution_1426():
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr += list(map(int, input().split()))
    arr.sort()
    
    K = int(input())
    arr1 = sorted(map(int, input().split()))
    
    i, j, c = N * M - 1, K - 1, 0
    while i >= 0 and j >= 0:
        if arr[i] >= arr1[j]:
            i -= 1
            j -= 1
            c += 1
        else:
            j -= 1
    return c


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=1436#1
def solution_1436():
    N = int(input())
    arr = list(map(int, input().split()))
    flag = False
    for i in range(1, N):
        if arr[i - 1] > arr[i]:
            flag = True
            break
    if flag:
        for i in range(1, N):
            prev = arr.copy()
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            
            if prev != arr:
                print(*arr)


# https://informatics.msk.ru/mod/statements/view.php?id=271&chapterid=1446#1
def solution_1446():
    N = int(input())
    arr = []
    for _ in range(N):
        pid, score = map(int, input().split())
        arr.append((pid, score))
    arr.sort(key=lambda x: (-x[1], x[0]))

    for pid, score in arr:
        print(pid, score)


# https://informatics.msk.ru/mod/statements/view.php?id=1129#1
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def solution_1129(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)

            if pi - 1 - low > high - (pi + 1):
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
            else:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))


# https://informatics.msk.ru/mod/statements/view.php?id=1129&chapterid=1418#1
def solution_1418():
    N = int(input())
    print(*len(set(map(int, input().split()))))


# https://informatics.msk.ru/mod/statements/view.php?id=1121#1
def solution_1442():
    N = int(input())

    i, j = 1, 1
    result = 0
    for _ in range(N):
        if i ** 2 == j ** 3:
            result = i ** 2
            i += 1
            j += 1
        elif i ** 2 < j ** 3:
            result = i ** 2
            i += 1
        else:
            result = j ** 3
            j += 1

    print(result)


# https://informatics.msk.ru/mod/statements/view.php?id=1121&chapterid=766#1
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left + i]
    for i in range(n2):
        R[i] = arr[mid + i + i]
    
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n1:
        arr[k] = L[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# https://informatics.msk.ru/mod/statements/view.php?id=1121&chapterid=767#1
def solution_767():
    N = int(input())
    arr1 = sorted(map(int, input().split()))
    M = int(input())
    arr2 = sorted(map(int, input().split()))

    i = j = 0

    while i < N and j < M:
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        else:
            return "NO"

    while i < N and arr1[i] == arr1[i - 1]:
        i += 1
    while j < M and arr2[j] == arr2[j - 1]:
        j += 1

    return "YES" if i == N and j == M else "NO"