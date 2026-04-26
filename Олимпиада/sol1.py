class Solution:
    def twoSum(self, arr, target):
        hash_table = {target - v: v for v in arr}
        for v in arr:
            if hash_table[v]:
                return True
        return False