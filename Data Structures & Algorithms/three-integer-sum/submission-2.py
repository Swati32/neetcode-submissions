class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Only works if nums are sorted 

        nums.sort()
        result = set()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    triplet = (nums[i], nums[l], nums[r])
                    result.add(triplet)
                    l += 1
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1

        return list(result)
