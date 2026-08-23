class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        no_of_zeros = 0
        for num in nums:
            if num != 0:
                product = num * product
            else:
                no_of_zeros += 1

        result = [0] * len(nums)
        
        if no_of_zeros == 1:
            for i,num in enumerate(nums):
                if num == 0:
                    result[i] = product
        elif no_of_zeros == 0:
            for i,num in enumerate(nums):
                remainder = product // num 
                result[i] = remainder
        
        return result
            
        