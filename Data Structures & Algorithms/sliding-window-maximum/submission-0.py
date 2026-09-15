class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        q = deque()
        result = []

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if q[0] < i - k + 1: # check if index has expired. So if window is 2 and q[0] is 0 and we are at i = 2. we already at 3rd element. regarless of queue size
                q.popleft()

            if i -k + 1 >=0: #check if window is size k to get result
                result.append(nums[q[0]])

        return result
        