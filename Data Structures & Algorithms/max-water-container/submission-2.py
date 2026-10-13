class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            width = r - l
            curr_water = min(heights[l], heights[r]) * width
            max_water = max(max_water, curr_water)

            # Ditch the bottleneck
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water