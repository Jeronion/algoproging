from heapq import *
from typing import List
from collections import Counter

class MinHeap:

    def __init__(self):
        self.arr = []

    def left(self, i): 
        return 2 * i + 1

    def right(self, i): 
        return 2 * i + 2

    def parent(self, i): 
        return (i - 1) // 2

    def get_min(self):
        return self.arr[0] if self.arr else None

    def insert(self, k):
        self.arr.append(k)
        i = len(self.arr) - 1

        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def decrease_key(self, i, new_val):
        self.arr[i] = new_val

        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_min(self):
        if len(self.arr) <= 0: 
            return None
        if len(self.arr) == 1: 
            return self.arr.pop()

        res = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.min_heapify(0)
        return res

    def delete_key(self, i):
        self.decrease_key(i, -float('inf'))
        self.extract_min()

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        n = len(self.arr)

        smallest = i

        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify_max(nums)
        for _ in range(k - 1):
            heappop_max(nums)
        return nums[0]
    
    def nthUglyNumber(self, n: int) -> int:
        # не ебу как оно здесь оказалось
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
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        hash_table = Counter(nums)
        return nlargest(k, hash_table.keys(), key=hash_table.get)

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for i, s in enumerate(score):
            heappush(heap, (-s, i))
        
        res = ["" for _ in range(len(score))]
        
        if heap:
            res[heappop(heap)[1]] = "Gold Medal"
        if heap:
            res[heappop(heap)[1]] = "Silver Medal"
        if heap:
            res[heappop(heap)[1]] = "Bronze Medal"
        
        rank = 4
        while heap:
            res[heappop(heap)[1]] = str(rank)
            rank += 1
        
        return res