class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left , right = 0, len(nums)-1

        while left < right:
            sum_pointers = nums[left] + nums[right]
            if  sum_pointers == target:
                return [left+1, right+1]
            if  sum_pointers > target:
                right -= 1
            else:
                left += 1

        return [left, right]

        