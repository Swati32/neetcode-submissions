class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # worst case eating speed

        while l <= r:
            mid = (l+r) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            if total_hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res
            
    
            
                
            
        