from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right in range(len(nums)):
            # 1. Process / Evaluate: check incoming element against the valid window
            if nums[right] in window:
                return True

            # 2. Expand: include incoming element
            window.add(nums[right])

            # 3. Shrink: evict the outgoing element once window exceeds span k
            if right >= k:
                window.remove(nums[right - k])

        return False