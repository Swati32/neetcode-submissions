class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, current_sum, path):
            if current_sum == target:
                res.append(list(path))
                return 
   
            for i in range(start, len(nums)):
                if current_sum+nums[i] > target:
                    break
                path.append(nums[i])
                dfs(i, current_sum+nums[i], path)
                path.pop()

        dfs(0, 0,[])
        return res