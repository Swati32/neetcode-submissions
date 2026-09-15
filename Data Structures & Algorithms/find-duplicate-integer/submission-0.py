class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle and find the collision point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]           # 1 step
            fast = nums[nums[fast]]     # 2 steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]           # 1 step from crash spot
            slow2 = nums[slow2]         # 1 step from start

        return slow
