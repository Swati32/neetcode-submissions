from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices

        for right, val in enumerate(nums):
            # 1. Maintain decreasing monotonic queue
            while q and nums[q[-1]] < val:
                q.pop()
            q.append(right)

            left = right - k + 1

            # 2. Expire leader if it fell off the left edge
            if q[0] < left:
                q.popleft()

            # 3. Record answer once the full window exists
            if left >= 0:
                output.append(nums[q[0]])

        return output