class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fmap = {}
        L = 0
        max_fruit = 0

        for R in range(len(fruits)):
            fmap[fruits[R]] = fmap.get(fruits[R], 0) + 1
            
            while len(fmap) > 2 and L < len(fruits):
                fmap[fruits[L]] = fmap.get(fruits[L], 0) - 1
                if fmap[fruits[L]] <= 0:
                    del fmap[fruits[L]]
                L += 1

            max_fruit = max(max_fruit, sum(fmap.values()))

        return max_fruit
            