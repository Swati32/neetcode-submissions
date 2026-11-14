class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Always binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2        # Corresponding cut in B

        """
        num1: [ ... num1_left  |  num1_right ... ]
        num2: [ ... num2_left  |  num2_right ... ]

        Think of half as a fixed-size shopping bag picking how many you take from pile 1 
        automatically decides how many you must take from pile 2.
        i = (l + r) // 2 (Items taken from nums1): Binary search guesses a cut point i in nums1—
        meaning we put the first i elements of nums1 into our left-half bag.
        
        j = half - i (Remaining items needed from nums2): Since the bag needs half elements in total
        and nums1 already contributed i of them, nums2 must contribute the exact remainder (half - i)
        elements (nums2[0 ... j-1]) so the total on the left side always equals half.    
        """
        l, r = 0, m
        while l <= r:
            num1_cut = (l + r) // 2
            num2_cut = half - num1_cut

            # 2. Extract edge values around the partition
            num1_left  = nums1[num1_cut - 1] if num1_cut > 0 else float("-inf")
            num1_right = nums1[num1_cut]     if num1_cut < m else float("inf")

            num2_left  = nums2[num2_cut - 1] if num2_cut > 0 else float("-inf")
            num2_right = nums2[num2_cut]     if num2_cut < n else float("inf")

            # 3. Valid partition: left half elements <= right half elements
            if num1_left <= num2_right and num2_left <= num1_right:
                if total % 2:
                    return float(max(num1_left, num2_left))
                return (max(num1_left, num2_left) + min(num1_right, num2_right)) / 2.0
            
            # 4. Binary search adjustments
            if num1_left > num2_right:
                r = num1_cut - 1
            else:
                l = num1_cut + 1
        return 0.0