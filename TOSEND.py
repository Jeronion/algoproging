N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

mns = {}
mxs = [[]] * M


for i in range(N):
    min_i = min(matrix[i])
    for j in range(M):
        if matrix[i][j] == min_i:
            mns[i].setdefault(i, []).append[j]

for i in range():
    