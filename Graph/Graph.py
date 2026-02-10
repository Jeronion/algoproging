from collections import deque
import heapq


def dijkstra_with_path(adj, src):
    V = len(adj)

    pq = []
    dist = [float("inf")] * V
    parent = [-1] * V   # для восстановления пути

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u          # запоминаем, откуда пришли
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


def get_path(parent, src, dest):
    path = []
    cur = dest

    while cur != -1:
        path.append(cur)
        if cur == src:
            break
        cur = parent[cur]

    if path[-1] != src:
        return []  # пути нет

    return path[::-1]



# https://informatics.msk.ru/mod/statements/view.php?id=11743#1
def solution_11743():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    graph = [[j + 1 for j in range(N) if grid[i][j]] for i in range(N)]
    for i in range(N):
        if not graph[i]:
            graph[i] = [0]
    for row in graph:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112629#1
def solution_112629():
    N = int(input())
    grid = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        row = list(map(int, input().split()))
        if not row[0]:
            continue
        else:
            for j in row:
                grid[i][j - 1] = 1
    
    for row in grid:
        print(*row)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112630#1
def solution_112630():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    c = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if grid[i][j] or grid[j][i]:
                c += 1
    
    print(c)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112631#1
def solution_112631():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    c = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if grid[i][j] == grid[j][i]:
                c += grid[i][j]
            else:
                c += grid[i][j] + grid[j][i]
    
    print(c)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112632#1
def solution_112632():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    c = [0, 0]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if grid[i][j] == grid[j][i] != 0:
                c[1] += 1
                continue
            if grid[i][j]:
                c[0] += 1
            if grid[j][i]:
                c[0] += 1
    print(*c)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112633#1
def solution_112633():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    arr = list(map(int, input().split()))
    res = 0
    for i in range(1, len(arr)):
        if grid[arr[i - 1] - 1][arr[i] - 1]:
            res += grid[arr[i - 1] - 1][arr[i] - 1]
        else:
            return 0
    return res


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112634#1
def solution_112634():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    graph = [[j for j in range(N) if grid[i][j]] for i in range(N)]
    visited = set()
    stack = [0]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)

            for u in reversed(graph[v]):
                if u not in visited:
                    stack.append(u)
    print("YES" if len(visited) == N else "NO")


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112635#1
def solution_112635():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    graph = [[j for j in range(N) if grid[i][j]] for i in range(N)]
    visited = [0] * (N)
    c = 0
    i = 0
    while i < N:
        if visited[i]:
            i += 1
            continue
        stack = [i]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 1

                for u in reversed(graph[v]):
                    if not visited[u]:
                        stack.append(u)
        c += 1

    print(c)


# https://informatics.msk.ru/mod/statements/view.php?id=11743&chapterid=112637#1
def solution_112637():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    graph = [[j for j in range(N) if grid[i][j]] for i in range(N)]
    
    K = int(input())
    pairs = set()
    
    for i in range(N):
        queue = deque()
        queue.append((i, 0))
        visited = set()
        
        while queue:
            v, d = queue.popleft()
            visited.add(v)
            
            if d == K + 1:
                if i < v:
                    pairs.add((i + 1, v + 1))
                continue
            
            for u in graph[v]:
                if u not in visited:
                    queue.append((u, d + 1))
    
    if not pairs:
        print(0)
    else:
        for a, b in sorted(pairs):
            print(a, b)