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

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=wmnj9rqt
def removeDuplicates(nums: List[int]) -> int:
    slow = 1
    for fast in range(len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow 


# https://leetcode.com/problems/remove-element/?envType=problem-list-v2&envId=wmnj9rqt
def removeElement(nums: List[int], val: int) -> int:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] == val:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=problem-list-v2&envId=wmnj9rqt
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


# https://leetcode.com/problems/merge-sorted-array/?envType=problem-list-v2&envId=wmnj9rqt
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    l, r = m - 1, n - 1
    while l >= 0 and r >= 0:
        if nums1[l] >= nums2[r]:
            nums1[l + r + 1] = nums1[l]
            l -= 1
        else:
            nums1[l + r + 1] = nums2[r]
            r -= 1
    
    while r >= 0:
        nums1[l + r + 1] = nums2[r]
        r -= 1



# https://leetcode.com/problems/valid-palindrome/?envType=problem-list-v2&envId=wmnj9rqt
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            right -= 1
            left += 1
    return True


# https://leetcode.com/problems/valid-triangle-number/?envType=study-plan-v2&envId=binary-search
def triangleNumber(nums: List[int]) -> int:
    c = 0
    n = len(nums)
    nums.sort()
    for i in range(n - 1, -1, -1):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                c += right - left
                right -= 1
            else:
                left += 1
    return c


# https://leetcode.com/problems/3sum-closest/?envType=problem-list-v2&envId=wmnj9rqt
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    N = len(nums)
    res = nums[0] + nums[1] + nums[2]
    for i in range(N - 2):
        l = i + 1
        r = N - 1
        while l < r:
            total = nums[l] + nums[r] + nums[i]
            if total == target:
                return target
            elif total < target:
                l += 1
            else:
                r -= 1
            if abs(total - target) < abs(target - res):
                res = total
    
    return res


# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/?envType=study-plan-v2&envId=binary-search
def numSubseq(nums, target):
    mod = 10**9 + 7
    nums.sort()
    n = len(nums)
    
    power = [1] * n
    for i in range(1, n):
        power[i] = (power[i - 1] * 2) % mod
    
    left, right = 0, n - 1
    result = 0
    
    while left <= right:
        if nums[left] + nums[right] <= target:
            result = (result + power[right - left]) % mod
            left += 1
        else:
            right -= 1
    
    return result


# https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=wmnj9rqt
def sortColors(nums: List[int]) -> None:
    left, right = 0, len(nums) - 1
    mid = 0
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = 0, nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = 2, nums[right]
            right -= 1
        else:
            mid += 1