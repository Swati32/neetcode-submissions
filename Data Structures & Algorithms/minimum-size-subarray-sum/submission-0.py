class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_len = math.inf
        sum_nums = 0
        result = 0
        for R in range(len(nums)):
            sum_nums += nums[R]

            while sum_nums >= target:
                min_len = min(min_len, R-L+1)
                sum_nums -= nums[L]
                L += 1

        result = 0 if min_len == math.inf else min_len
        return result
 
