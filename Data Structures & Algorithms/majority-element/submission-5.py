class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = None
        votes = 0

        for num in nums:
            if num == winner:
                votes += 1
            elif votes == 0:
                winner = num
                votes = 1
            else:
                votes -= 1

        return winner
