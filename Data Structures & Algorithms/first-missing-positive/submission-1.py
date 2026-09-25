from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # =========================================================================
        # PARKING LOT RULES:
        # Array indices 0 to n-1 are Spots 0 to n-1.
        # Car #1 belongs in Spot 0, Car #2 in Spot 1... Car #x in Spot (x - 1).
        # Negative numbers (e.g. -2) and 0 have NO permit (0 < nums[i] <= n fails),
        # so they stay parked wherever they are and get skipped.
        # =========================================================================
        for i in range(n):
            # Keep swapping while:
            # 1. nums[i] is a valid car with a reserved spot in our lot (1 to n)
            # 2. nums[i] is not already parked in its correct spot
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                
                # -----------------------------------------------------------------
                # PYTHON TRAP AVOIDED:
                # We MUST cache target_idx first.
                # If we wrote: nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                # Python assigns from LEFT to RIGHT:
                # 1. nums[i] gets overwritten FIRST.
                # 2. Then nums[nums[i]-1] evaluates with the NEW value of nums[i],
                #    sending the car to the completely wrong spot -> Infinite loop!
                # -----------------------------------------------------------------
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # =========================================================================
        # INSPECTION ROUND:
        # Check spots in order: Spot 0, Spot 1, Spot 2...
        # Spot `i` expects Car `i + 1`.
        # =========================================================================
        for i in range(n):
            # If Spot `i` has a negative number (-2), a duplicate, or wrong car,
            # it means Car `i + 1` never showed up to the parking lot at all!
            if nums[i] != i + 1:
                return i + 1
        
        # If Cars 1 through n are all parked correctly, the missing one is n + 1.
        return n + 1