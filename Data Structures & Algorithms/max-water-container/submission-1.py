class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l # cause width btw say 0 & 1 is 1-0 = 1. not num of elements
            area = height * width
            max_area = max(max_area, area)

            if heights[l] < heights[r] :
                l += 1
            else:
                r -= 1
        
        return max_area
        