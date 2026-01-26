import sys

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