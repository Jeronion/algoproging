n = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [[[0] for _ in range(n)] for _ in range(n)]
