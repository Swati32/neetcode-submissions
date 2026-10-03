class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum = sum(nums)
        lsum = 0
        for i, num in enumerate(nums):
            if tsum - num - lsum == lsum :
                return i
            lsum += num
        return -1
            

        