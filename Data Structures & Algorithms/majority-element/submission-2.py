class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        winner = nums[0]
        votes = 1
        
        for num in nums[1:]:  
            if votes == 0:
                winner = num      
            votes= votes + 1 if winner == num else votes - 1
            
        return winner 