n, q = map(int, input().split())
A = [list(map(int, input().split())) + [0] for _ in range(n)]
K = [int(input()) for _ in range(q)]

for i in range(1, n):
    A[i][2] += A[i - 1][2]
    A[i][2] += min(A[i][0] - A[i - 1][0], A[i - 1][1])
    A[i][1] += max(0, A[i - 1][1] - A[i][0] + A[i - 1][0])

for j in K:
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if A[m][0] < j:
            l = m + 1
        else:
            r = m - 1
    if l == 0:
        print(0)
    else:
        print(A[l - 1][2] + min(j - A[l - 1][0] + 1, A[l - 1][1]))