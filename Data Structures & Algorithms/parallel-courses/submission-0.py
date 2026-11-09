class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        indegree = [0] * (n+1)

        for dependent, course in relations:
            indegree[dependent] += 1
            adj[course].append(dependent)
        
        queue = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        
        semesters = 0
        courses_taken = 0

        while queue:
            semesters += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                courses_taken += 1

                for neighbor in adj[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        # If we couldn't take all courses, there was a cycle
        return semesters if courses_taken == n else -1