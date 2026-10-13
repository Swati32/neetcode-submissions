class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: 
            return

        n = len(nums) # do not use len(nums-1) here
        k = k % n

        def reverse(l,r): # reverse with index
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1 
        
        reverse(0, n-1) # reverse entire array 4,5,6,7,1,2,3
        reverse(0, k-1) # reverse first k i.e 0,k-1  3,2,1,4,5,6,7
        reverse(k, n-1) # reverse rest k till n-1 3,2,1,7,6,5,4
        

    '''
       Left Rotation by k (Shift Left):
           reverse(0, k - 1) (flip first k)
           reverse(k, n - 1) (flip the rest)
           reverse(0, n - 1) (flip whole array)

       Right Rotation
            Reverse the entire array: reverse(0, n - 1)
            Reverse the first k elements: reverse(0, k - 1)
            Reverse the remaining n - k elements: reverse(k, n - 1)
       '''
        

        