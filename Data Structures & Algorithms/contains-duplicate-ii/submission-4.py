class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        
        seen = {}
       
        for i in range(len(nums)): 
            seen[nums[i]] = seen.get(nums[i], 0) + 1

            if seen[nums[i]] > 1:
                return True

            if i >= k:
                outgoing = nums[i - k]
                seen[outgoing] -= 1

                if seen[outgoing] == 0:
                    del seen[outgoing]
        
        return False

        