class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            if cur_sum >= 0:
                cur_sum += nums[i]
                max_sum = max(cur_sum, max_sum)
            else:
                cur_sum = nums[i]
        
        return max(max_sum,cur_sum)

        