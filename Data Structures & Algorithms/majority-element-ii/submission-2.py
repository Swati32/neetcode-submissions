class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            Whenever a voter walks into the room, ask:
              Are you already supporting an active candidate? (Check matches)
              If not, is there an open podium? (Check count == 0)
              If neither, cancel out! (Subtract) 
        '''

        votes1 = 0
        votes2 = 0
        winner1 = None
        winner2 = None

        for num in nums:
            if winner1 == num:
                votes1 += 1
            elif winner2 ==num:
                votes2 += 1
            elif votes1 == 0:
                winner1 = num
                votes1 = 1
            elif votes2 == 0:
                winner2 = num
                votes2 = 1
            else:
                votes1 -= 1
                votes2 -= 1
        
        threshold = len(nums) // 3
        result = []
        for candidate in [winner1, winner2]:
            if candidate is not None and nums.count(candidate) > threshold:
                result.append(candidate)
        
        return result

