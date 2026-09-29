class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right in range(len(nums)):
            # 1. Process / Check incoming against the active window
            # 2. Expand: add to set

            if nums[right] in window:
                return True
            window.add(nums[right])

            # 3. Shrink: evict oldest once distance exceeds k
            if right >= k:
                window.remove(nums[right - k])

        return False