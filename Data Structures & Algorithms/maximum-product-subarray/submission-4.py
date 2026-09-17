class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far, min_so_far, max_res= 1, 1, nums[0]

        for num in nums:
            candidates = (num, num * max_so_far, num * min_so_far)
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            max_res = max(max_res, max_so_far)

        return max_res

            
        
