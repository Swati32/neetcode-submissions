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

                    square = (i//3 , j//3)

                    if (num in rows[i] or 
                        num in cols[j] or 
                        num in squares[square]):
                        return False
                    
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[square].add(num)
        return True
        