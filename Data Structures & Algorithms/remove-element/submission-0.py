class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        l, r = 0, n

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1

        return l
    