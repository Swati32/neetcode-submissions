class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: 
            return

        n = len(nums)-1 
        k = k % len(nums)


        def reverse(arr):
            l, r = 0, len(arr)-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+= 1
                r -=1
            return arr
            
        
        nums[:n-k+1] = reverse(nums[:n-k+1])
        nums[n-k+1:] = reverse(nums[n-k+1:])
        reverse(nums)

        