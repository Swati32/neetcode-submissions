class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        for i in range(len(nums)) : 
            seen = set()

            for j in range(i+1, len(nums)):
                needed = -(nums[i] + nums[j])

                if needed in seen:
                    triplet = tuple(sorted([nums[i], nums[j], needed]))
                    result.add(triplet)
            
                seen.add(nums[j])
        
        return list(result)