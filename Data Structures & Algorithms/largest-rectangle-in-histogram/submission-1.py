class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0) # dummy node
        stack = []

        for i, h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                width = i - idx
                max_area = max(max_area, height * width)
                start = idx

            stack.append((start, h))

        return max_area

            
            
        

        