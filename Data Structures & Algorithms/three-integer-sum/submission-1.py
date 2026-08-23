class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    triplet = tuple([nums[i], nums[l], nums[r]])
                    result.add(triplet)
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return list(result)
