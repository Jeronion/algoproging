n, q = map(int, input().split())
A = [list(map(int, input().split())) + [0] for _ in range(n)]
K = [int(input()) for _ in range(q)]


for i in range(1, n):
    A[i][1] += A[i - 1][1] - (A[i][0] - A[i - 1][0])
    if A[i][1] < 0:
        A[i][1] = 0

print(*A)

for j in K:
    l, r = 0, n
    while l <= r:
        m = (l + r) // 2
        if m < n and A[m][0] <= j:
            l = m + 1
        else:
            r = m - 1
    if r < 0:
        print(0)
    else:
        if A[r][1] + A[r][0] - j > 0:
            print(A[r][1] + A[r][0] - j)
        else:
            print(0)
# 1000000000000000000