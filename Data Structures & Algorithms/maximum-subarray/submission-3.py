class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L, R = 0, 0
        max_sum = -math.inf
        curr_sum = 0

        while L <= R and R < len(nums):
            curr_sum += nums[R]
            max_sum = max(max_sum, curr_sum)
            R += 1
            if curr_sum < 0:
                curr_sum = 0
                L = R
    
        return max_sum
        








        
