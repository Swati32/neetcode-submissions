class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                    left = j+1
                    right = len(nums) - 1
                    need = target - nums[i] - nums[j]
                    while left < right:
                        sum = nums[left] + nums[right]
                        if sum == need:
                            result.add((nums[i], nums[j], nums[left], nums[right]))
                            left += 1
                            right -= 1
                        elif sum < need:
                            left += 1
                        else:
                            right -= 1
        
        return list(result)
        