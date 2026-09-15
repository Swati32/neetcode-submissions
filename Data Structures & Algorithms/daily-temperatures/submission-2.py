class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append((i,temperature))
           
        
        return res


        