class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        bfs he. complication is humne begin word daal dia par word by word compare kaise kare
        sare words ko set me daalon. queue me daalon begin words. ab sare letters in word ke liye 
        sare letters of alphaber se letteer ko replace karo and check karo if word set me he ya nai. 
        he toh step badao and queue me dalon. as soon as popped endword ho return step 
        '''
        words = set(wordList)
        if endWord not in words:
            return 0

        # (word, step_count)
        queue = deque([(beginWord, 1)])
        # Remove beginWord to avoid revisiting
        if beginWord in words:
            words.remove(beginWord)

        alpha = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            popped, step = queue.popleft()
            if popped == endWord:
                return step
            
            for i, letter in enumerate(popped):
                for ch in alpha:
                    if ch == letter:
                        continue
                    new_word = popped[:i]+ch+popped[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        queue.append((new_word, step+1))
        return 0
