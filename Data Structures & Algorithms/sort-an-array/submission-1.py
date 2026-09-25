class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #  merge sort
        """
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr  # return arr not []

            mid = len(arr) // 2 # either len(arr)//2 or (right-left+1) // 2

            left_merge = merge_sort(arr[:mid])
            right_merge = merge_sort(arr[mid:])

            return merge(left_merge, right_merge)

        def merge(left, right):
            l = 0
            r = 0
            merged = []

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            merged += left[l:]
            merged += right[r:]

            return merged
        
        return merge_sort(nums)
        """

        n = len(nums)

        def sift_down(length: int, root: int) -> None:
            """
            Restores the max-heap property for the subtree rooted at `root`.
            Pushes the element at `root` down until both its children are smaller.
            """
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            # Check if the left child exists and is larger than current largest
            if left < length and nums[left] > nums[largest]:
                largest = left

            # Check if the right child exists and is larger than current largest
            if right < length and nums[right] > nums[largest]:
                largest = right

            # If a child was larger, swap and keep sifting down the affected subtree
            if largest != root:
                nums[root], nums[largest] = nums[largest], nums[root]
                sift_down(length, largest)
        # ------------------------------------------------------------------
        # Phase 1: Build the Max-Heap (Bottom-Up)
        # ------------------------------------------------------------------
        # Start at the last parent (n // 2 - 1) and move backward to the root (0).
        # We skip leaves (indices n // 2 to n - 1) because they have no children.
        for i in range(n // 2 - 1, -1, -1):
            sift_down(n, i)

        # ------------------------------------------------------------------
        # Phase 2: Extract the Max to the End One-by-One
        # ------------------------------------------------------------------
        # nums[0] is always the largest element in the remaining unsorted heap.
        # Swap it to the back (end), lock it in place, and repair the heap.
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]  # Move current max to end
            sift_down(end, 0)                        # Only root (index 0) is broken

        return nums