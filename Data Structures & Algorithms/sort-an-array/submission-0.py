class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #  merge sort

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

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