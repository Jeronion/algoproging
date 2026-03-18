from array import array

# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=201#1
def count_ways_1_or_2_steps():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N - 1]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=203#1
def count_ways_1_2_3_steps():
    N = int(input())
    if N == 0:
        return 0
    dp = [0] * (N + 2)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N + 1):
        dp[i] = sum(dp[i - 3: i])
    return dp[N]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=842#1
def fibonacci_last_digit():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10
    return dp[N]


# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=843#1
def strange_recursive_sequence():
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
def binary_tree_nodes_sequence():
    N = int(input())
    a = [0] * (N + 1)
    a[0], a[1] = 1, 1

    for i in range(2, N + 1):
        if i % 2 == 0:
            a[i] = a[i // 2] + 1
        else:
            a[i] = a[i // 2 + 1] + a[i // 2] + 1

    return a[N]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=914#1
def count_domino_tilings_variant():
    N = int(input())
    dp = [1] * (N + 1)
    dp[1] = 3
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) * 2
    return dp[-1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=915#1
def min_cost_path_linear():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, N):
        arr[i] += min(arr[i - 1], arr[i - 2])
    return arr[N - 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=2963#1

def min_operations_to_one():
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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112503#1
def generate_ugly_numbers():
    N = int(input())
    numbers = [1]
    i2, i3, i5 = 0, 0, 0
    for _ in range(N):
        next2 = numbers[i2] * 2
        next3 = numbers[i3] * 3
        next5 = numbers[i5] * 5
        next_num = min(next2, next3, next5)
        numbers.append(next_num)
        
        if next_num == next2:
            i2 += 1
        if next_num == next3:
            i3 += 1
        if next_num == next5:
            i5 += 1
    
    print(*numbers[1:])


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i_2, i_3, i_5 = 0, 0, 0
        for _ in range(n - 1):
            curr = min(nums[i_2] * 2, nums[i_3] * 3, nums[i_5] * 5)
            nums.append(curr)
            if nums[i_2] * 2 == curr:
                i_2 += 1
            if nums[i_3] * 3 == curr:
                i_3 += 1
            if nums[i_5] * 5 == curr:
                i_5 += 1
        return nums[-1]