class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = 1
        min_so_far = 1
        max_res = -math.inf
        for num in nums:
           
            temp_max = max(num * max_so_far, num * min_so_far, num)
            min_so_far = min(num * max_so_far, num * min_so_far, num)

            max_so_far = temp_max
            max_res = max(max_res, max_so_far)

        return max_res

            
        
