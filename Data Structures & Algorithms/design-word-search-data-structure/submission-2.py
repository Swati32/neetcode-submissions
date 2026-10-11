class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end_of_word

            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
            
            if ch in node.children:
                return dfs(i+1, node.children[ch])
            
            return False
        
        return dfs(0, self.root)
                
