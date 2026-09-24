from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        # prefix table has size (m + 1) x (n + 1)
        # Row 0 and Col 0 remain 0 as boundary padding.
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        """
        Visualizing prefix[r][c]:
        
        (0,0)             c-1       c
          +----------------+-------+
          |                |       |
          |  OVERLAP       | ABOVE |  <- Both 'ABOVE' and 'LEFT' include 'OVERLAP'
          |                |       |
          +----------------+-------+ r-1
          |  LEFT          |   X   |  <- X is matrix[r - 1][c - 1]
          +----------------+-------+ r
          
        To compute prefix[r][c] (sum of rectangle from (0,0) to (r-1, c-1)):
          1. Add the current matrix element: matrix[r - 1][c - 1]
          2. Add the block directly above:   + prefix[r - 1][c]
          3. Add the block to the left:      + prefix[r][c - 1]
          4. Subtract the overlap corner:    - prefix[r - 1][c - 1] (counted twice)
        """

        # Loop through prefix coordinates starting from (1, 1)
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.prefix[r][c] = (
                    matrix[r - 1][c - 1]         # Current cell value in original matrix
                    + self.prefix[r - 1][c]      # Entire block directly above
                    + self.prefix[r][c - 1]      # Entire block directly to the left
                    - self.prefix[r - 1][c - 1]  # Overlap block counted in both above & left
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        MATRIX INDICES:
               col 0      ...     col1 - 1       col1       ...       col2
             +--------------------------------+----------------------------+
             |                                |                            |
             |                                |                            |
         ... |        overlap_corner          |         top_strip          |  <- Roof to chop off
             |                                |                            |     (rows 0 .. row1 - 1)
             |                                |                            |
        row1-1|                                |                            |
             +--------------------------------+----------------------------+
             |                                | ************************** |
        row1 |                                | *                        * |
             |                                | *                        * |
         ... |          left_strip            | *         TARGET         * |
             |                                | *                        * |
        row2 |                                | ************************** |
             +--------------------------------+----------------------------+


        PREFIX LOOKUP GEOMETRY (Box Dimensions from (0,0)):

                                col1 columns wide              col2 + 1 columns wide
                                      |                                  |
                                      v                                  v
         (0,0)                        |                                  |
           +--------------------------+----------------------------------+
           |                          |                                  |
           |      overlap_corner      |            top_strip             |
           |                          |                                  |
           +--------------------------+----------------------------------+ <--- row1 rows tall
           |                          |                                  |
           |        left_strip        |              TARGET              |
           |                          |                                  |
           +--------------------------+----------------------------------+ <--- row2 + 1 rows tall


        LOOKUP TABLE MAPPING:
        +------------------+-----------------------+-----------------------+-----------------------------+--------+
        | Component        | Matrix Region         | Dimensions (H x W)    | Prefix Lookup               | Action |
        +------------------+-----------------------+-----------------------+-----------------------------+--------+
        | full_box         | (0,0) to (row2, col2) | (row2 + 1) x (col2 + 1)| prefix[row2 + 1][col2 + 1]  |   +    |
        | top_strip        | (0,0) to (row1-1,col2)| row1       x (col2 + 1)| prefix[row1][col2 + 1]      |   -    |
        | left_strip       | (0,0) to (row2,col1-1)| (row2 + 1) x col1     | prefix[row2 + 1][col1]      |   -    |
        | overlap_corner   | (0,0) to (row1-1,col1-1)| row1     x col1     | prefix[row1][col1]          |   +    |
        +------------------+-----------------------+-----------------------+-----------------------------+--------+
        """
        # Map boundaries to prefix dimensions (height and width counts)
        top = row1
        left = col1
        bottom = row2 + 1
        right = col2 + 1

        # 1. Total box containing everything down to (row2, col2)
        full_box = self.prefix[bottom][right]

        # 2. Roof to chop off: rows 0 through (row1 - 1)
        top_strip = self.prefix[top][right]

        # 3. Left wall to chop off: cols 0 through (col1 - 1)
        left_strip = self.prefix[bottom][left]

        # 4. Overlap corner: rows 0 through (row1 - 1), cols 0 through (col1 - 1)
        #    Subtracted twice by top_strip and left_strip; must add back once
        overlap_corner = self.prefix[top][left]

        return full_box - top_strip - left_strip + overlap_corner