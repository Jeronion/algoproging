from array import array

# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=201#1
def solution_201():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N - 1]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=203#1
def solution_203():
    N = int(input())
    if N == 0:
        return 0
    dp = [0] * (N + 2)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N + 1):
        dp[i] = sum(dp[i - 3: i])
    return dp[N]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=842#1
def solution_842():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10
    return dp[N]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=843#1
def solution_843():
    N = int(input())
    a = [0] * (N + 1)
    a[0], a[1] = 1, 1
    for i in range(2, N + 1):
        if i % 2:
            a[i] = a[i // 2] - a[i // 2 - 1]
        else:
            a[i] = a[i // 2] + a[i // 2 - 1]
    
    return a[N]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=844#1
def solution_844():
    N = int(input())
    a = [0] * (N + 1)
    a[0], a[1] = 1, 1

    for i in range(2, N + 1):
        if i % 2 == 0:
            a[i] = a[i // 2] + 1
        else:
            a[i] = a[i // 2 + 1] + a[i // 2] + 1

    return a[N]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=207#1
def solution_207():
    N = int(input())
    dp = [1] * (N + 2)
    for i in range(2, N + 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N + 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=912#1
def solution_912():
    N = int(input())
    dp = [1] * (N + 2)
    dp[2] = 2
    for i in range(3, N + 2):
        dp[i] = sum(dp[i - 3: i])
    return dp[N + 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=913#1
def solution_913():
    N = int(input())
    dp = [1] * (N + 2)
    for i in range(2, N + 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N + 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=914#1
def solution_914():
    N = int(input())
    dp = [1] * (N + 1)
    dp[1] = 3
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) * 2
    return dp[-1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=915#1
def solution_915():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, N):
        arr[i] += min(arr[i - 1], arr[i - 2])
    return arr[N - 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=2963#1

def solution_2963():
    N = int(input())
    if N == 1:
        print('')
        return

    dp = bytearray(N + 1)
    prev = array('i', [0]) * (N + 1)
    op = bytearray(N + 1)  # будем хранить коды: 1,2,3

    for x in range(2, N + 1):
        dp[x] = dp[x - 1] + 1
        prev[x] = x - 1
        op[x] = 1

        if x % 2 == 0 and dp[x // 2] + 1 < dp[x]:
            dp[x] = dp[x // 2] + 1
            prev[x] = x // 2
            op[x] = 2

        if x % 3 == 0 and dp[x // 3] + 1 < dp[x]:
            dp[x] = dp[x // 3] + 1
            prev[x] = x // 3
            op[x] = 3

    res = []
    cur = N
    while cur != 1:
        res.append(str(op[cur]))
        cur = prev[cur]

    print(''.join(reversed(res)))