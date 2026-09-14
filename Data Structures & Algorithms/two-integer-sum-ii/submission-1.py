class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L , R = 0, len(nums)-1

        while L < R:
            sum_pointers = nums[L] + nums[R]
            if  sum_pointers == target:
                return [L+1, R+1]
            if  sum_pointers > target:
                R-= 1
            else:
                L += 1

        return [-1, -1]

        