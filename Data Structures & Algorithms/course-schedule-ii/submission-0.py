class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []

        while queue:
            popped = queue.popleft()
            result.append(popped)
            numCourses -= 1

            for c in adj[popped]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        
        return [] if numCourses else result
            

        