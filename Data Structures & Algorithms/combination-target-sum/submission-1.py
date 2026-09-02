class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, nums[j] + total)
                cur.pop()                 
        dfs(0, [], 0)
        return res