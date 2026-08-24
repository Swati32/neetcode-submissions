class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we are looking for num which is less than both
        # left and right side of array nums
        # i.e min number in rotated sorted array

        left = 0 
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]

    
        