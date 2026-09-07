class Solution:
    def rob(self, nums: List[int]) -> int:     
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            rob1, rob2 = 0, arr[0]
            i = 1
            while i < len(arr):
                temp = rob2
                rob2 = max(rob2, rob1+ arr[i])
                rob1 = temp
                i += 1
            return rob2
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))