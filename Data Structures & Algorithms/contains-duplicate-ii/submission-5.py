class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        
        seen = set()
       
        for i in range(len(nums)): 
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])

            if i >= k:
                outgoing = nums[i - k]
                seen.remove(outgoing)
        
        return False

        