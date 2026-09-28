class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1 = m-1
        idx2 = n-1
        last_idx = m+n-1

        while last_idx >= 0:
            if idx2 >= 0:
                if idx1 >= 0 and nums1[idx1] >= nums2[idx2]:
                    nums1[last_idx] = nums1[idx1]
                    idx1 -= 1
                else:
                    nums1[last_idx] = nums2[idx2]
                    idx2 -= 1
            last_idx -=1 
        
        
                    


        



        