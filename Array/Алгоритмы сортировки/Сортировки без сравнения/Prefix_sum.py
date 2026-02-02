# https://www.geeksforgeeks.org/dsa/equilibrium-index-of-an-array/
def findEquilibrium(arr):
    N = len(arr)
    prefix_sum = [0] * N
    prefix_sum[0] = arr[0]
    
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    for i in range(N):
        if prefix_sum[i - 1] == prefix_sum[N - 1] - prefix_sum[i]:
            return i


# https://www.geeksforgeeks.org/dsa/mean-range-array/
def findMean(arr, queries):
    N = len(arr)
    Q = len(queries)
    result = []
    
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        pref[i] = pref[i - 1] + arr[i - 1]
    
    for i in range(Q):
        l = queries[i][0]
        r = queries[i][1]
        n = r - l + 1
        result.append((pref[r + 1] - pref[l]) / n)
    
    return result


# https://www.geeksforgeeks.org/dsa/find-original-array-from-given-prefix-sum-array/
def decode_array(presum):
    arr = [0] * len(presum)
    arr[0] = presum[0]
    for i in range(1, len(presum)):
        arr[i] = presum[i] - presum[i - 1]
    
    return arr




def minSubArrayLen(target: int, nums: list[int]) -> int:
    res = float("inf")
    pref = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        pref[i] = pref[i - 1] + nums[i - 1]
    
    left, right = 0, 1
    while right < len(nums) + 1:
        s = pref[right] - pref[left]
        if s >= target:
            res = min(res, right - left)
            left += 1
        else:
            right += 1
    
    return res if res != float("inf") else 0



def productExceptSelf(nums: list[int]) -> list[int]:
    output = [0] * len(nums)

    pref = [1] * (len(nums) + 1)
    for i in range(len(nums)):
        pref[i] = pref[i - 1] * nums[i]
    suff = [1] * (len(nums) + 1)
    for i in range(len(nums) - 1, -1, -1):
        suff[i] = suff[i + 1] * nums[i]
    
    for i in range(len(nums)):
        output[i] = pref[i - 1] * suff[i + 1]
    return output