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
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                if word[j] != ".":
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
                else:
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False 
                
            return curr.end_of_word

        return dfs(0, self.root)
