class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for ch in word:
                adj[ch] = set()

        indegree = {}
        for ch in adj:
            indegree[ch] = 0

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break    
                
        queue = deque([])
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
                
        res = []
        while queue:
            ch = queue.popleft()
            res.append(ch)

            for nr in adj[ch]:
                indegree[nr] -= 1
                if indegree[nr] == 0:
                    queue.append(nr)

        if len(res) != len(indegree):
                return ""

        return "".join(res)