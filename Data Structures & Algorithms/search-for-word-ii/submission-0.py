class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end_of_word = True
        
        ROW, COL = len(board), len(board[0])
        visited, res = set(), set()

        def dfs(root, word_till_now, row, col):
            if (row < 0 or col < 0 or row >= ROW or col >= COL or (row, col) in 
            visited or  board[row][col] not in root.children):
                return
            
            new_word = word_till_now + board[row][col]
            new_root = root.children[board[row][col]]

            if new_root.end_of_word:
                res.add(new_word)

            visited.add((row, col))
            dfs(new_root, new_word, row+1, col)
            dfs(new_root, new_word, row-1, col)
            dfs(new_root, new_word, row, col+1)
            dfs(new_root, new_word, row, col-1)

            visited.remove((row, col))

        for i in range(ROW):
            for j in range(COL) :
                dfs(root, "", i, j)

        return list(res)