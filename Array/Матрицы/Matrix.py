# https://informatics.msk.ru/mod/statements/view.php?id=11404#1
def solution_112363():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    S = 0
    for i in range(N):
        for j in range(M):
            S += grid[i][j]
    return S


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112364#1
def solution_112364():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    c = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == K:
                c += 1
    return c


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112365#1
def solution_112365():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    R = int(input())
    c = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] // (10 ** (K - 1)) and sum(map(list(grid[i][j]))) % R == 0:
                c += 1
    
    return c


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112366#1
def solution_112366():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    M, m = [0, 0, float("-inf")], [0, 0, float("inf")]
    for i in range(N):
        for j in range(M):
            if grid[i][j] > M[2]:
                M = [i, j, grid[i][j]]
            if grid[i][j] < m[2]:
                M = [i, j, grid[i][j]]

    return M, m


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112367#1
def solution_112367():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    S = [sum(grid[0]), 0]
    for i in range(1, N):
        if sum(grid[i]) < S[0]:
            S = [sum(grid[i]), i]
    return grid[S[1]]


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112368#
def solution_112368():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    mx = max([max(i) for i in grid])
    res = []
    for i in range(M):
        for j in range(N):
            if grid[j][i] == mx:
                res.append(i)
                break
    
    for j in res:
        to_print = [0] * N
        for i in range(N):
            to_print[i] = grid[i][j]
        print(*to_print)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112369#
def solution_112369():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            grid[i][j] = 0
    
    for row in grid:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112370#1
def solution_112370():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if grid[i][j] != grid[j][i]:
                return "NO"
    return "YES"


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112371#1
def solution_112371():
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    row_mins = [min(row) for row in matrix]
    col_maxs = [max(matrix[i][j] for i in range(N)) for j in range(M)]

    saddle_points = []

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                saddle_points.append((i+1, j+1))
    
    if saddle_points:
        for point in saddle_points:
            print(point[0], point[1])
    else:
        print(0)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112372#1
def solution_112372():
    N, M = map(int, input().split())
    grid = [[int(i % 2 != j % 2) for j in range(M)] for i in range(N)]
    for row in grid:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112373#1
def solution_112373():
    N, M = map(int, input().split())
    grid = [[i + j for j in range(M)] for i in range(N)]
    for row in grid:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112374#1
def solution_112374():
    N, M = map(int, input().split())
    grid = [[abs(i - j) for j in range(M)] for i in range(N)]
    for row in grid:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11404&chapterid=112375#1
def solution_112374():
    N, M = map(int, input().split())
    grid = [[(M * i) + (j + 1 if i % 2 == 0 else M - j) for j in range(M)] for i in range(N)]
    for row in grid:
        print(*row, sep='\t')

solution_112374()