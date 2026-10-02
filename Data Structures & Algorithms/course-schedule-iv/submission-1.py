class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)
        in_degree = [0] * numCourses
        prereq_map = defaultdict(set)

        for course, dependent in prerequisites:
            adj[course].append(dependent)
            in_degree[dependent] += 1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            popped = queue.popleft()
            for neighbor in adj[popped]:
                prereq_map[neighbor].add(popped)
                prereq_map[neighbor].update(prereq_map[popped])

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Har query instant O(1) me check hogi
        return [u in prereq_map[v] for u, v in queries]      
                
