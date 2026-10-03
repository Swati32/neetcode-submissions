from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        [0 ------------------------ Purana Cut point ------------------------- Current End (j)]
        |<---------------- Purana Sum (needed) ---->|<------- Desired Chunk (k) ------------->|
        |<---------------------------- Total Rassi = running_sum --------------------------->|
        '''

        psum = {0:1}
        rsum = 0
        count = 0

        for num in nums:
            rsum += num
            needed = rsum - k
            if needed in psum:
                count += psum[needed] 
            psum[rsum] = psum.get(rsum, 0) + 1
        
        return count
            

        