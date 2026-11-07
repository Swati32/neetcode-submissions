class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Always binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2        # Corresponding cut in B

        """
        A: [ ... A_left  |  A_right ... ]
        B: [ ... B_left  |  B_right ... ]

        """
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = half - i

            # 2. Extract edge values around the partition
            A_left  = nums1[i - 1] if i > 0 else float("-inf")
            A_right = nums1[i]     if i < m else float("inf")
            B_left  = nums2[j - 1] if j > 0 else float("-inf")
            B_right = nums2[j]     if j < n else float("inf")

            # 3. Valid partition: left half elements <= right half elements
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # 4. Binary search adjustments
            if A_left > B_right:
                r = i - 1
            else:
                l = i + 1
        return 0.0