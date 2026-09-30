class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr)-1

        while L <= R and R-L+1 > k :
            if abs(arr[L] - x) <= abs(arr[R]- x):
                R -= 1
            else:
                L += 1
            
        return arr[L: R+1]






        