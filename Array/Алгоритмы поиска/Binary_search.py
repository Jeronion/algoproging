from math import *
from bisect import *
from heapq import *
from collections import *
from itertools import *
from time import *
from sys import *

from typing import (
    List,
    Optional,
    Dict,
    Set,
    Tuple,
    Deque,
    DefaultDict,
    Any,
    Callable,
    Iterable,
)

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def searchInsertLeft(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left


def nextGreatestLetter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    return letters[0] if letters[mid] < target else letters[mid]


def guess(n: int) -> int:
    # return -1 if num is higher than the picked number
    # 1 if num is lower than the picked number
    # otherwise return 0
    pass


def guessNumber(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) < 0:
            right = mid - 1
        else:
            left = mid + 1


# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=2#1
def solution_2():
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    to_search = map(int, input().split())
    
    for x in to_search:
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == 0:
            print(array[0])
        elif left == N:
            print(array[N - 1])
        else:
            l = array[left - 1]
            r = array[left]
            if abs(l - x) <= abs(r - x):
                print(l)
            else:
                print(r)


# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=4#1
def solution_3():
    N = int(input())
    c = 0
    while N - 1:
        N = N // 2 + (N % 2)
        c += 1
    print(c)


# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=4#1
def solution_4():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    to_search = map(int, input().split())
    
    for x in to_search:
        result = "NO"
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
            else:
                result = "YES"
                break
        print(result)


# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=111728#1
def solution_111728():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for x in map(int, input().split()):
        result = [None, None]
        left, right = 0, N - 1
        # right
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == N:
            print(0); continue
        if arr[left] != x:
            print(0); continue
        
        result[0] = left + 1 if left != N else left
        left, right = 0, N - 1
        # left
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        result[1] = left
        print(*result)


# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=study-plan-v2&envId=binary-search
def countNegatives(grid: List[List[int]]) -> int:
    counter = 0
    n, m = len(grid) - 1, 0
    while m < len(grid[0]) and n > -1:
        if grid[n][m] < 0:
            counter += len(grid[0]) - m
            n -= 1
        else:
            m += 1
    return counter


# https://leetcode.com/problems/valid-perfect-square/?envType=study-plan-v2&envId=binary-search
# solution 1
def isPerfectSquare(num: int) -> bool:
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < num:
            left = mid + 1
        elif mid * mid == num:
            return True
        else:
            right = mid - 1
    return False


# solution 2
def isPerfectSquare(self, num: int) -> bool:
    x = num
    while x * x >= num:
        x = (x + num // x) // 2
    return x * x == num


def isBadVersion(bad):
    pass

# https://leetcode.com/problems/first-bad-version/?envType=study-plan-v2&envId=binary-search
def firstBadVersion(n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=binary-search
def mySqrt(x: int) -> int:
    num = x
    while x * x > num:
        x = (x + num // x) // 2
    return x 


# https://leetcode.com/problems/arranging-coins/description/?envType=study-plan-v2&envId=binary-search
def arrangeCoins(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if (mid + 1) * mid // 2 > n:
            right = mid - 1
        else:
            left = mid + 1
    return right


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=binary-search
def searchRange(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    
    if left == len(nums):
        return result
    if nums[left] != target:
        return result
    
    result[0] = left
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    result[1] = left - 1
    return result


# https://leetcode.com/problems/find-right-interval/description/?envType=study-plan-v2&envId=binary-search
def findRightInterval(intervals: List[List[int]]) -> List[int]:
    sorted_intervals = sorted(enumerate(intervals), key=lambda x: x[1][0])
    result = [-1] * len(intervals)
    
    for i in range(len(intervals)):
        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_intervals[mid][1][0] >= intervals[i][1]:
                right = mid - 1
            else:
                left = mid + 1
        
        if left == len(intervals):
            continue
        if left == 0 and sorted_intervals[left][1][0] < intervals[i][1]:
            continue
        result[i] = sorted_intervals[left][0]
    
    return result


# https://informatics.msk.ru/mod/statements/view.php?id=1966#1
def solution_1923():
    w, h, n = map(int, input().split())
    left, right = max(w, h), max(w * n, h * n) + 1
    while left <= right:
        mid = (left + right) // 2
        if -(-n // (mid // w)) * h <= mid and -(-n // (mid // h)) * w <= mid:
            right = mid - 1
        else:
            left = mid + 1
    return left


# https://informatics.msk.ru/mod/statements/view.php?id=1129&chapterid=1418#1
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=binary-search
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    left, right = 0, len(matrix) - 1
    i = -1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            i = mid
            break
        elif matrix[mid][0] > target:
            right = mid - 1
        else:
            left = mid + 1
    if i == -1:
        return False
    
    left, right = 0, len(matrix[i]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[i][mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    
    if matrix[i][left] == target:
        return True
    return False


# informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1#1
def checking(arr, x, k):
    j, c = 0, 1
    for i in range(1, len(arr)):
        if arr[i] >= arr[j] + x:
            j = i
            c += 1
    return c >= k
        

def solution_1():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    left, right = 1, arr[-1] - arr[0]
    while left <= right:
        mid = (left + right) // 2
        if checking(arr, mid, K):
            left = mid + 1
        else:
            right = mid - 1
    return right


# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=binary-search
def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
    
    return nums[left]


# https://leetcode.com/problems/h-index-ii/?envType=study-plan-v2&envId=binary-search
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] >= n - mid:
            right = mid - 1
        else:
            left = mid + 1
    return n - left


# https://leetcode.com/problems/single-element-in-a-sorted-array/?envType=study-plan-v2&envId=binary-search
def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid + 1] != nums[mid]:
            right = mid
        else:
            left = mid + 2
    return nums[left]


# https://leetcode.com/problems/peak-index-in-a-mountain-array/?envType=study-plan-v2&envId=binary-search
def peakIndexInMountainArray(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    if len(arr) == 1:
        return 0
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


# https://leetcode.com/problems/find-k-closest-elements/?envType=study-plan-v2&envId=binary-search
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]