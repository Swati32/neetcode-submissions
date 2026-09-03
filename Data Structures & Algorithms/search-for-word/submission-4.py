class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row, col , word_till_now):

            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                return False

            if (row, col) in visited:
                return False

            curr_word = word_till_now + board[row][col]

            if not word.startswith(curr_word):
                return False

            if curr_word == word:
                return True
            
            visited.add((row, col))
            if (dfs(row+1, col, curr_word) or
                dfs(row-1, col, curr_word) or
                dfs(row, col+1, curr_word) or
                dfs(row, col-1, curr_word)):
                    return True
            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,""):
                    return True
        return False