class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        row_zero = False
        col_zero = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                
                    if i == 0:
                        row_zero = True
                    if j == 0:
                        col_zero = True

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0 

        for j in range(1, n):
            if row_zero:
                matrix[0][j] = 0

        for i in range(1, m):
            if col_zero:
                matrix[i][0] = 0

        
        