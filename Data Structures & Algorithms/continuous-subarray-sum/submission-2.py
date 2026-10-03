class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        [0 ----------------------- Index i (Purana Cut) ------------------------- Index j (Current)]
        |<------- Remainder r --------->|<---------------- Subarray (Multiple of k) -------------->|
        |<------------------------------ Poori Rassi = running_sum -------------------------------->|
        '''

        psum = {0: -1}
        rsum = 0
        for i, num in enumerate(nums):
            rsum += num
            needed = rsum % k

            if needed in psum:
                if abs(psum[needed]-i) >= 2:
                    return True
            else:
                psum[needed] = i

        return False