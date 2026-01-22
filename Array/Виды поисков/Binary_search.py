from ...Imports import *

"""Список ссылок решенных задач:

https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search
https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=binary-search
"""

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