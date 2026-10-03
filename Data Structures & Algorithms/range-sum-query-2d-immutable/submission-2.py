class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.psum = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.psum[i][j] = self.psum[i-1][j] + self.psum[i][j-1] - self.psum[i-1][j-1] + matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full_box = self.psum[row2+1][col2+1]
        left_box = self.psum[row1][col2+1]
        right_box = self.psum[row2+1][col1]
        overlap = self.psum[row1][col1]

        '''
        col1         col2 + 1
             +-------------+-------------+
        row1 |   overlap   |     TOP     |
             +-------------+-------------+
    row2 + 1 |    LEFT     |  FULL_BOX   |
             +-------------+-------------+
        '''
        return full_box - left_box - right_box + overlap
    