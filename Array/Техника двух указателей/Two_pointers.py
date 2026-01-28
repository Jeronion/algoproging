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