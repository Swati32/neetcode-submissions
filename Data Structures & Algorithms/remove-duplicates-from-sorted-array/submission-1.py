class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        With r incrementing by for lopp
        l == r do nothing 
        l != r increment left and then swap
        return last swap + 1 i.e left + 1
        '''
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1