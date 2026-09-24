class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        """
        +-----------+---+
        | OVERLAP   |   |
        | OVERLAP   |   |  <- Counted in Box Above AND counted in Box to Left!
        | OVERLAP   |   |
        +-----------+---+
        |           | X |

        So to get the complete new box:
        Start with the current single number: matrix[r][c]
        Add the whole block above: + self.prefix[r][c + 1]
        Add the whole block to the left: + self.prefix[r + 1][c]
        Subtract the overlap counted twice: - self.prefix[r][c]
        """

        for r in range(m):
            for c in range(n):
                self.prefix[r + 1][c + 1] = (matrix[r][c] +
                    self.prefix[r][c+1] +
                    self.prefix[r+1][c] +   
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    # Translating to 1-indexed prefix table coordinates:
    # A matrix boundary at index `x` maps to:
    # - Bottom/Right inclusive edge -> `x + 1`
    # - Top/Left slice boundary-> `x` (i.e., excludes index `x` by stopping at `x - 1 + 1`)
        
    # 1. Total box from (0, 0) to bottom-right target corner (row2, col2)
        full_box = self.prefix[row2 + 1][col2 + 1]
        
    # 2. Unwanted top strip (everything above row1)
        top_strip = self.prefix[row1][col2 + 1]
        
    # 3. Unwanted left strip (everything left of col1)
        left_strip = self.prefix[row2 + 1][col1]
        
    # 4. Overlap corner (subtracted twice in steps 2 and 3; must add back)
        overlap_corner = self.prefix[row1][col1]
        
        return full_box - top_strip - left_strip + overlap_corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)