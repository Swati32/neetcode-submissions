class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}
        for word in words:
            for ch in word:
                adj[ch] = set()
                indegree[ch] = 0
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
            
        res = []
        queue = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
            
        while queue:
            popped = queue.popleft()
            res.append(popped)

            for ch in adj[popped]:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    queue.append(ch)
            
        if len(indegree) == len(res):
            return "".join(res)
        else:
            return ""
