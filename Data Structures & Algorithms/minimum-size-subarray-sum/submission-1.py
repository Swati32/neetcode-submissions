class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_len = math.inf
        sum_nums = 0
        for R in range(len(nums)):
            sum_nums += nums[R]
            print(sum_nums)
            while sum_nums >= target:
                min_len = min(min_len, R-L+1)
                print(f"updated min len {min_len}")
                sum_nums -= nums[L]
                L += 1

        return min_len if min_len != math.inf else 0
 
