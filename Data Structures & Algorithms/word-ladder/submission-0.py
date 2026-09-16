class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        # (word, step_count)
        queue = deque([(beginWord, 1)])
        # Remove beginWord to avoid revisiting
        words.discard(beginWord)

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
