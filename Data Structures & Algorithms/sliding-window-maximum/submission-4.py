class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for R in range(len(nums)):
            # 1. Expand: maintain decreasing order by popping smaller elements from the back
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            # 2. Shrink: evict the front index if it has fallen outside window size k
            # Because the window has a fixed length of k ending at index R, its valid span covers indices from R - k + 1 up to R
            # Too old / Expired: Any index at or to the left of R - k
            # The Check: q[0] is the index of the current maximum. If q[0] <= R - k, that maximum belonged to an earlier window and must be dropped from the front via popleft().
            if q[0] <= R - k:
                q.popleft()
            
            if R >= k - 1: #0 indexed
                result.append(nums[q[0]])

        return result
            

            



            
        