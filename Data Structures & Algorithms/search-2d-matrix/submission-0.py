class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = (l+r)//2

            mid_row = mid // cols
            mid_col = mid % cols

            if matrix[mid_row][mid_col] == target:
                return True
            elif target > matrix[mid_row][mid_col] :
                l = mid +1
            else:
                r = mid -1
        
        return False

        