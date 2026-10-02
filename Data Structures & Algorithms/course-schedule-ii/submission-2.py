class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for dependent, course in prerequisites:
            indegree[dependent] += 1
            adj[course].append(dependent)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        result = []
     
        while queue:
            for i in range(len(queue)):
                popped = queue.popleft()
                result.append(popped)

                for dependent in adj[popped]:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        queue.append(dependent)
        
        return result if numCourses == len(result) else []
                    
            

        