class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                    num = board[i][j]
                    if num == ".":
                        continue
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    square = (i//3 , j//3)
                    if num in squares[square]:
                        return False
                    squares[square].add(num)
        return True
        